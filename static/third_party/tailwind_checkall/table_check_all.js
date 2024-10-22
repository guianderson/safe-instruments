document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('masterCheckbox').addEventListener('change', function () {
        const checkboxes = document.querySelectorAll('.itemCheckbox');
        checkboxes.forEach(checkbox => checkbox.checked = this.checked);
    });

    const checkboxes = document.querySelectorAll('.itemCheckbox');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            const masterCheckbox = document.getElementById('masterCheckbox');
            masterCheckbox.checked = Array.from(checkboxes).every(checkbox => checkbox.checked);
        });
    });

});
