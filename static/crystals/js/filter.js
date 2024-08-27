document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('crystal-filter-form');
    const searchInput = document.getElementById('search-input');
    const showActive = document.getElementById('show-active');
    const showInactive = document.getElementById('show-inactive');

    function submitForm() {
        form.submit();
    }

    searchInput.addEventListener('input', submitForm);
    showActive.addEventListener('change', submitForm);
    showInactive.addEventListener('change', submitForm);
});