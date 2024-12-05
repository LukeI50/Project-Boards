const editButtons = document.getElementsByClassName("btn-task-edit");
const taskText = document.getElementById("id_body");
const taskForm = document.getElementById("taskForm");
const submitButton = document.getElementById("submitButton");

/**
 * Initialises edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated task's ID upon
 * click.
 * - Fetches the content of the corresponding task.
 * - Populates the `taskContent` input/textarea with 
 * the task's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */
for (let button of editButtons){
    console.log(editButtons)
    button.addEventListener("click", (e) => {
        let taskId = e.target.getAttribute("task_id");
        let taskContent = document.getElementById(`task${taskId}`).innerText;
        taskText.value = taskContent;
        submitButton.innerText = "Update";
        taskForm.setAttribute("action", `edit_comment/${commentId}`);
    })
}