var tasks = document.getElementById("ul");

var addTask = function(){
    let string = document.getElementsByClassName("newTask")[0].value;
    if(string === ""){
        alert("Task is empty!");
        return;
    }
    let newItem = document.createElement("li");

    let newInput = document.createElement("input");
    let newP = document.createElement("p");
    let newBtn = document.createElement("button");

    newP.innerHTML = string;
    newP.classList.add("taskText");

    newInput.classList.add("taskCheckbox");
    newInput.setAttribute("type", "checkbox");


    newBtn.id = document.getElementsByTagName("li").length+1;
    newItem.id = "task_" + newBtn.id;


    newBtn.innerText = "Done";
    newBtn.classList.add("taskBtn");
    newBtn.setAttribute("onClick", "removeTask(this.id)");
    newItem.appendChild(newInput);
    newItem.appendChild(newP);
    newItem.appendChild(newBtn);
    
    let tasks = document.getElementById("ul");
    tasks.appendChild(newItem);

    document.getElementsByClassName("newTask")[0].value = "";
}

var removeTask = function(index){
    let tasks = document.getElementsByTagName("li");
    for (let i = 0; i < tasks.length; i++) {
        const element = tasks[i];
        if(element.id == "task_"+index)
            index = i;
    }
    let target = tasks[index];
    document.getElementById("ul").removeChild(target);
}