var data = {}

const imageReceived = e => {
    console.log(e)
    //var img = document.getElementById("test-img").src = downloadedImg
}

window.addEventListener("load", function() {
    var mySocket = new WebSocket("ws://localhost:8080");
    mySocket.onmessage = function (event) {
        var output = document.getElementById("output");
        
        // put text into our output div
        output.textContent = event.data;
        js = JSON.parse(event.data.replaceAll("'", '"'));
        if (data != js) {
            data = js
            console.log("new data found!");
            console.log(data)
            let downloadedImg = new Image;
            downloadedImg.crossOrigin = "Anonymous";
            downloadedImg.addEventListener("load", imageReceived, false);
            downloadedImg.src = data.media;
            
        } 
    };

    function makeData() {
        console.log("Making data!")
        mySocket.send("");
        setTimeout(makeData, 100);
    }
    makeData()
});