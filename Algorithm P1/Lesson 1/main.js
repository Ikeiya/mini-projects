var list = [1, 4, 7, 8, 9, 11, 17, 23, 27, 30]
var linearTrial = [0, "notFound"]
var binaryTrial = [0, "notFound"]
var number = null

function main(input){
    if (input == "linear")  {
        linearTrial = linearSearch(number, linearTrial[0])
    }   else if (input == "binary") {
        binaryTrial = binarySearch(number, binaryTrial[0])
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
    console.log(number)
};

function linearSearch(number, linearTrial){
    if (number == list[linearTrial]){
        return [linearTrial+1, "valueFound"]
    }   else    {
        return [linearTrial+1, "notFound"]
    }
}

function binarySearch(number, binaryTrial){
    if (number == list[binaryTrial]){
        return [binaryTrial, "valueFound"]
    }   else if (number > list[binaryTrial])    {
        return [Math.floor(binaryTrial+(binaryTrial/2)), "notFound"]
    }   else    {
        return [Math.floor(binaryTrial/2), "notFound"]
    }
}
