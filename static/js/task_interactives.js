document.addEventListener("DOMContentLoaded", () => {
    const editButtons = document.getElementsByClassName("btn-task-edit");
    const deleteButtons = document.getElementsByClassName('btn-delete');

    const tastText = document.getElementById('id_content');
    const taskForm = document.getElementById("taskForm");
    const addTaskModal = new bootstrap.Modal("#AddTaskModal");

    const deleteTaskModal = new bootstrap.Modal("#DeleteTaskModal");
    const deleteConfirm = document.getElementById("deleteConfirm");

    const modalTitle = document.getElementById('AddTaskModalTitle');
    const toastHeaders = document.getElementsByClassName('toast-header')
    console.log(modalTitle);

    const submitButton = document.getElementById("submitButton");

    console.log("task edit script successfully loaded")


    // Initialise edit buttons 
    for (let button of editButtons){
        button.addEventListener("click", (e) => {
            const taskId = e.target.getAttribute('data-task_id');
            console.log("task Id is: " + taskId)
            console.log("button clicked");

            // Identify task area
            const task = document.getElementById(`task${taskId}`);
            // retrieve relevant data
            const title = task.children[1].firstElementChild.textContent;
            const content = task.querySelector('.toast-body p.d-none').textContent;
            const status = task.querySelector('.toast-body p:first-child').getAttribute('data-task-status');
            console.log(title)

            // complete form
            document.getElementById('id_taskTitle').value = title;
            document.getElementById('id_content').value = content;
            document.getElementById('id_status').value = status;

            let testel = document.getElementById('id_taskTitle');
            console.log(title)
            console.log(testel)

            modalTitle.innerText = "Edit Task";
            submitButton.innerText = "Update";
            taskForm.action = `${window.location.pathname}edit_task/${taskId}`;

            addTaskModal.show();

        })
        
        // Initialise makeshift on hover function
        // button.addEventListener("mouseover", () => {
        //     console.log("mousedover")
        //     hovertime = setTimeout(() => {
        //         console.log("start hovertimer");
        //         button.classList.remove('bg-info');
        //         button.classList.add("bg-danger");
        //         console.log(button.innerHTML);

        //         const result = "Delete";
        //         let count = 0;

        //         button.innerHTML = "";
        //         console.log("emtied html?", button.innerHTML)
        //         let valueToUpdate = ["", ""];

        //         const deleteStyle = setInterval(() => {
        //             console.log("in deleting style")
        //             if (button.innerText == "Delete") {
        //                 clearInterval(deleteStyle);
        //             } else {
        //                 console.log("count =", count)
        //                 console.log(`letter to be added ${result[count]}`)
        //                 valueToUpdate[1] = result[count];

        //                 button.innerText = valueToUpdate.join("")
        //                 valueToUpdate[0] = valueToUpdate.join("")
        //                 count++;
        //             }
        //         }, 50);

                
                
                
        //     }, 2500)
        //     // might be able to trap it in a whileloop that way.
            
        //     initialHtml = '<i task_id="{{ task.id }}" class="fa-solid fa-pencil"></i>';
            
        //     // maybe try creating a while loop in which the mouseout can exist
        //     button.addEventListener("mouseout", () => {
        //         console.log("mousedout")
        //         clearTimeout(hovertime)
        //         if (button.classList.contains('bg-danger')) {
        //             button.classList.remove('bg-danger');
        //             button.classList.add('bg-info');
        //         }
        //         button.innerText = "Edit";
        //         button.innerHTML = initialHtml;
        //     })
            
        // })

    }

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            console.log("delete clicked")
            let taskId = e.target.getAttribute("data-task_id");
            console.log(taskId)
            deleteConfirm.href = `${window.location.pathname}delete_task/${taskId}`;
            deleteTaskModal.show();
        })
    }

})
