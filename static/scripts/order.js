orderedBydate = document.getElementsByClassName("logs");

document.getElementById("cryptoProfits").addEventListener("click",
    function() {
        console.log("The button is active!");
        logs = document.getElementsByClassName("logs");

        orderedList = []
        unordererdList = []
        for(let x = 0; x < logs.length; x++) {
            orderedList.push(parseFloat(logs[x].children[3].innerHTML.split("$")[1]));
            unordererdList.push(parseFloat(logs[x].children[3].innerHTML.split("$")[1]));
        }
        orderedList.sort(function(a, b) {return a - b;})

        console.log(orderedList.findIndex(rank => rank === 94.31));
        
        completedList = []
        for(let x = 0; x < orderedList.length; x++) {
            completedList.push(logs[unordererdList.findIndex(rank => rank === orderedList[x])])
        }

        console.log(completedList)

        for(let x = 0; x < completedList.length; x++) {
            logs[x].innerHTML = completedList[x].innerHTML
        }
    }  
)

