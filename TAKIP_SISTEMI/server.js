const aedes = require("aedes")();
const server = require("net").createServer(aedes.handle);
const express = require("express");
const http = require("http");
const WebSocket = require("ws");

const PORT_MQTT = 1883;
const PORT_HTTP = 3000;

server.listen(PORT_MQTT, () => {
  console.log(`✅ MQTT broker running on port ${PORT_MQTT}`);
});

const app = express();
const httpServer = http.createServer(app);
const wss = new WebSocket.Server({ server: httpServer });

app.use(express.static("public"));

// WebSocket bağlantısı
wss.on("connection", (ws) => {
  console.log("New client connected");
  ws.send(JSON.stringify({ message: "Connected to tracker!" }));
});

// MQTT Mesajlarını Al ve WebSocket Üzerinden Gönder
aedes.on("publish", (packet) => {
  const message = packet.payload.toString();
  const regex = /LAT:(-?\d+\.\d+)LON:(-?\d+\.\d+)/;
  const match = message.match(regex);

  if (match) {
    const data = {
      lat: parseFloat(match[1]),
      lon: parseFloat(match[2]),
      timestamp: new Date().toISOString(),
    };

    console.log(`📡 MQTT Mesajı Alındı:`, data);

    // WebSocket ile tüm istemcilere konumu gönder
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify(data));
      }
    });
  }
});

httpServer.listen(PORT_HTTP, () => {
  console.log(`🚀 Web interface running on http://localhost:${PORT_HTTP}`);
});
