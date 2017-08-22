//d3.json("http://localhost:8000/api/v1/yieldsfanalysis/?format=json", function (data){
//    var width = 500
//    var height = 300
//    var padding = 20
//    
//    d3.select("body")
//    .append("svg")
//    .attr("class", "scattercontainer")
//    .attr("width", width)
//    .attr("height", height)
//    .attr("style", "outline: thin solid black")
//    
//    var xScale = d3.scaleLinear()
//                    .domain([0, d3.max(data, function(d){
//                        return d.seat_factor;
//                    })])
//                    .range([padding, width - padding])
//    var yScale = d3.scaleLinear()
//                .domain([0, d3.max(data, function(d){
//                    return d.route_yield;
//                })])
//                .range([padding, height - padding])
//    
//    d3.select("svg")
//    .selectAll("circle")
//    .data(data)
//    .enter()
//    .append("circle")
//        .attr("cx", function(d){
//        return xScale(d.seat_factor);
//    })
//        .attr("cy", function(d){
//        return yScale(d.route_yield);
//    })
//        .attr("r", 5)
//        .attr("fill", "black")
//    
//    d3.select("svg")
//        .selectAll("text")
//        .data(data)
//        .enter()
//        .append("text")

})