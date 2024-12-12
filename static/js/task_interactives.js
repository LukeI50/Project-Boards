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
