const http = require("node:http");
const server=http.createServer((req,res)=>{
    res.writeHead(200);
    res.end("Hospital Management System");
});
server.listen(3000,()=>{
    console.log("server running on portt 3000");
});

