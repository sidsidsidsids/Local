import express from "express"
import SocketIO from "socket.io"
import http from "http"

const app = express();

app.set("view engine", "pug")
app.set("views", __dirname + "/views");
app.use("/public", express.static(__dirname + "/public"));
app.get("/", (req, res) => res.render("home"));
app.get("/*", (req, res) => res.render("/"));


const server = http.createServer(app);
const io = SocketIO(server);

function publicRooms(){
    const {
        sockets: {
            adapter: { sids, rooms },
        },
    } = io
    // same as
    // const sids = io.sockets.adapter.sids;
    // const rooms = io.sockets.adapter.rooms;
    const publicRooms = [];
    rooms.forEach((_, key) => {
        if(sids.get(key) === undefined){
            publicRooms.push(key);
        }
    });
    return publicRooms;
}

function countRoom(roomName){
    return io.sockets.adapter.rooms.get(roomName)?.size
}

io.on("connection", socket => {
    socket["nickname"] = "Anonymous"
    socket.onAny((event) => {
        console.log(io.sockets.adapter)
        console.log(`Socket Event: ${event}`)
    })
    socket.on("enter_room", (roomName, done) => {
        socket.join(roomName);
        done(countRoom(roomName));
        socket.to(roomName).emit("welcome", socket.nickname, countRoom(roomName));
        io.sockets.emit("room_change", publicRooms())
    });
    socket.on("disconnecting", () => {
        socket.rooms.forEach((room) => socket.to(room).emit("bye", socket.nickname, countRoom(room) - 1));
    })
    socket.on("disconnect", () => {
        io.sockets.emit("room_change", publicRooms())
    })
    socket.on("new_message", (msg, room, done) => {
        socket.to(room).emit("new_message", `${socket.nickname}: ${msg}`);
        done()
    })
    socket.on("nickname", (nickname) => socket["nickname"] = nickname)
})

// function onSocketClose() {
//     console.log("Disconnected from server")
// }

// const sockets = []

// wss.on("connection", (socket) => {
//     sockets.push(socket);
//     socket["nickname"] = "Anonymous"
//     console.log("connected to browser");
//     socket.on("close", onSocketClose)
//     socket.on("message", (message) => {
//         const parsed = JSON.parse(message.toString("utf-8"))
//         switch(parsed.type){
//             case "new_message":
//                 sockets.forEach((aSocket) => 
//                     aSocket.send(`${socket.nickname}: ${parsed.payload}`)
//                     )
//                 break
//             case "nickname":
//                 socket["nickname"] = parsed.payload;
//                 break
//         }
//     })
// });
const handleListen = () => console.log(`Listening on http://localhost:3000`) 

server.listen(3000, handleListen)
