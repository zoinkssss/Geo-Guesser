window.addEventListener('load', function() {
    console.log('running');
    const canvasMap = document.getElementById('map_layer');
    canvasMap.width = document.documentElement.clientWidth * 0.8;
    canvasMap.height = document.documentElement.clientHeight * 0.8;
    class Pin {
        construstor(x, y) {
            this.x = x;
            this.y = y;
            this.color = 'white'
    }
    drawMarker(ctx) {
        ctx.save();
        ctx.translate(this.x,this.y)
        
        ctx.beginPath();
        ctx.moveTo(0,0);
        ctx.bezierCurveTo(2,-10,-20,-25,0,-30);
        ctx.beizerCurveTo(20,-25,-2, -10,0,0);
        ctx.fillStyle=this.color;
        ctx.fill();
        ctx.strokeStyle="black";
        ctx.lineWidth=1.5;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(0,-21,3,0,Math.PI*2);
        ctx.closePath();
        ctx.fillStyle="black"
        ctx.fill();

        ctx.restore();
    }
}

class Map {
    constructor(canvas) {
        this.canvas = canvas
        this.ctx = canvasMap.getContext('2d');
        this.pins = Array();
        this.mainPin = null
        this.images = getImages()
        this.activeMap = this.images.items(0);
    }
    setPin(pos) {
        this.mainPin = new Pin(pos.x, pos.y)
    }
    addPin(pos) { 
        let pin = new Pin(pos.x, pos.y)
        this.pins.push(pin)
    }

    drawActiveMap() {
        let image = this.activeMap
        this.ctx.save();

        let ratio = this.activeMap.naturalWidth / this.activeMap.naturalHeight

        this.ctx.translat(this.canvas.width/2,this.canvas.height/2);
        this.ctx.rotate(90*Math.PI/180);
        this.ctx.drawImage(this.activeMap, -this.canvas.height/2, -this.canvas.width/2, this.cancas.height, this.canvas.width);
        this.ctx.restore();
    }
    
draw() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height)
    this.drawActiveMap()
    this.mainPin.drawMarker(this.ctx);
   }

}

const map = new Map(canvasMap, );
map.setPin({
    x: 100,
    y: 100   
});

canvasMap.appEventListener('click', function(evt) {
    let mousePos = getMousePos(canvasMap, evt)
    map.setPin(mousePos);
}, false);

function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
}

function getImages() {
    let images = document.getElementByClassName('map_images');
    console.log(images);
    return images;
}

function drawImageProp(ctx, img, x, y, w, h, offsetX, offsetY) {
    if (arguments.length 2) {
        x = y = 0;
        w = ctx.canvas.width;
        h = ctx.canvas.height;
    }

    offsetX = typeof offsetX "number" ? offsetX : 0.5;
    offsetY = typeof offsetY "number" ? offsetY : 0.5;

    if (offsetX < 0) offsetX = 0;
    if (offsetY < 0) offsetY = 0;
    if (offsetX > 1) offsetX = 1;
    if (offsetY > 1) offsetY = 1;

    var iw = img.width 
        ih = img.height
        r = Math.min(w / iw, h / ih),
        nw = iw * r, 
        nh = ih * r, 
        cx, cy, cw, ch, ar = 1;

        if (nw < w) ar = w / nw;
        if (Math.abs(ar - 1) < 1e-14 && nh < h) ar = h /nh;
        nw *= ar;
        nh *= ar;

        cw = iw / (nw / w);
        ch = ih / (nh / h);

        if (cx < 0) cx = 0;
        if (cy < 0) cy = 0;
        if (cw > iw) cw = iw;
        if (ch > ih) ch = ih;

        ctx.drawImage(img, cx, cy, cw, ch, x, y ,w , h);

}
console.log(map)
function animate() {
    map.draw();
    requestAnimationFrame(animate);
}
animate();



});


