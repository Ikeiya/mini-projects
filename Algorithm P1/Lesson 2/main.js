var list = [1, 4, 7, 8, 9, 11, 17, 23, 27, 30, 39, 47, 52]
var linearTrial = [0, "notFound"]
var binaryTrial = [0, "notFound", 1]
var number = null

function main(input){
    console.log(binaryTrial)
    if (input == "linear")  {
        linearTrial = linearSearch(number, linearTrial[0])
    }   else if (input == "binary") {
        binaryTrial = binarySearch(number, binaryTrial[0], binaryTrial[2])
    }
    if (linearTrial == "valueFound") {
        console.log(linearTrial)
    }   else if (binaryTrial == "valueFound")   {
        console.log(binaryTrial)
    }
    console.log(linearTrial, binaryTrial)
}

function getValue(){
    number = document.getElementById("number").value;
    binaryTrial[0] = list.length
    binaryTrial[2] = 1
    console.log(number)
};

function linearSearch(number, linearTrial){
    if (number == list[linearTrial]){
        return [linearTrial+1, "valueFound"]
    }   else    {
        return [linearTrial+1, "notFound"]
    }
}

function binarySearch(number, binaryTrial, steps){
    steps++
    if (number == list[binaryTrial]){
        return [binaryTrial, "valueFound"]
    }   else if (number > list[binaryTrial])    {
        return [Math.ceil(binaryTrial+(binaryTrial/steps)), "notFound", steps]
    }   else    {
        return [Math.floor(binaryTrial-(binaryTrial/steps)), "notFound", steps]
    }
}
