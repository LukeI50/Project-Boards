document.addEventListener("DOMContentLoaded", () => {
    const editButtons = document.getElementsByClassName("btn-task-edit");

    const taskForm = document.getElementById("taskForm");
    const addTaskModal = document.getElementById("AddTaskModal");

    const submitButton = document.getElementById("submitButton");

    console.log("task edit script successfully loaded")


    // Initialise edit buttons
    for (let button of editButtons){
        button.addEventListener("click", (e) => {
            const taskId = e.target.getAttribute('task_id');
            const taskContent = document.getElementById(`task${taskId}`).innerText;
            
            





            taskText.value = taskContent;
            submitButton.innerText = "Update";
            taskForm.setAttribute("action", `edit_comment/${commentId}`);
        })
    }

})
