document.addEventListener("DOMContentLoaded", function() {
    // Get all edit buttons by their class name
    const editButtons = document.getElementsByClassName("btn-task-edit");
    // Get all delete buttons by their class name
    const deleteButtons = document.getElementsByClassName('btn-delete');

    // Get the task form element
    const taskForm = document.getElementById("taskForm");
    // Initialize the Bootstrap modal for adding tasks
    const addTaskModal = new bootstrap.Modal("#AddTaskModal");

    // Initialize the Bootstrap modal for deleting tasks
    const deleteTaskModal = new bootstrap.Modal("#DeleteTaskModal");
    // Get the delete confirmation link element
    const deleteConfirm = document.getElementById("deleteConfirm");

    // Get the modal title element
    const modalTitle = document.getElementById('AddTaskModalTitle');

    // Get the submit button element
    const submitButton = document.getElementById("submitButton");

    /**
     * Initialize edit buttons with event listeners.
     */
    for (const button of editButtons){
        button.addEventListener("click", (e) => {
            // Get the task ID from the data attribute
            const taskId = e.target.getAttribute('data-task_id');

            // Identify the task area by its ID
            const task = document.getElementById(`task${taskId}`);
            // Retrieve relevant data from the task element
            const title = task.children[1].firstElementChild.textContent;
            const content = task
            .querySelector('.toast-body p.d-none')
            .textContent;
            const status = task
            .querySelector('.toast-body p:first-child')
            .getAttribute('data-task-status');

            // Complete the form with retrieved data

            document.getElementById('id_taskTitle').value = title;
            document.getElementById('id_content').value = content;
            document.getElementById('id_status').value = status;

            // Set the modal title and submit button text for editing
            modalTitle.innerText = "Edit Task";
            submitButton.innerText = "Update";
            taskForm.action = `${window.location.pathname}edit_task/${taskId}`;

            // Show the add task modal
            addTaskModal.show();
        })

    };

    /**
     * Initialize delete buttons with event listeners.
     */
    for (button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let taskId = e.target.getAttribute("data-task_id");
            // Set the href attribute of the delete confirmation link
            deleteConfirm.href = `${window.location
                .pathname}delete_task/${taskId}`;
            deleteTaskModal.show();
        })
    };

})
