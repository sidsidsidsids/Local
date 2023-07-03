import express from "express"
import http from "http"
import { WebSocketServer } from "ws";

const app = express();

app.set("view engine", "pug")
app.set("views", __dirname + "/views");
app.use("/public", express.static(__dirname + "/public"));
app.get("/", (req, res) => res.render("home"));
app.get("/*", (req, res) => res.render("/"));

const handleListen = () => console.log(`Listening on http://localhost:3000`) 

const server = http.createServer(app);
const wss = new WebSocketServer({ server })

function onSocketClose() {
    console.log("Disconnected from server")
}

const sockets = []

wss.on("connection", (socket) => {
    sockets.push(socket);
    socket["nickname"] = "Anonymous"
    console.log("connected to browser");
    socket.on("close", onSocketClose)
    socket.on("message", (message) => {
        const parsed = JSON.parse(message.toString("utf-8"))
        switch(parsed.type){
            case "new_message":
                sockets.forEach((aSocket) => 
                    aSocket.send(`${socket.nickname}: ${parsed.payload}`)
                    )
                break
            case "nickname":
                socket["nickname"] = parsed.payload;
                break
        }
    })
});

server.listen(3000, handleListen)
