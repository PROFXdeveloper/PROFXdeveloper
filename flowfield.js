var points = []
var mult = 0.005

function setup(){
  createCanvas(windowWidth,windowHeight)
  background(30)
  angleMode(DEGREES)
  noiseDetail(1)
  var density= 30
  var space = width / density

  for (var x=0; x < width; x+= space){
    for (var y=0; y< height; y+= space){

      var p = createVector(x + random(-10,10),y + random(-10,10))
    points.push(p)


    }
  }
}
function draw (){
  noStroke()
  for (var i=0; i< points.length; i++){
   
    var r = map(points[i].x, 0, width, 50,255)
    var g = map(points[i].y, 0, height, 50,255)
    var b = map(points[i].x, 0, width, 255,50)
    var alpha = map(dist(width / 2, height / 2,points[i].x,points[i].y),0,300,250,0)

    fill(r,g,b,alpha)

    var angle = map(noise(points[i].x * mult,points[i].y* mult),0,1,0,720)
  


  points[i].add(createVector(cos(angle),sin(angle)))
  if (dist(width / 2, height / 2, points[i].x,points[i].y) < 300 ){
    ellipse(points[i].x,points[i].y,1)


    }
   }
  } 
