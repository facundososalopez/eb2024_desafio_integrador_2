(function() {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));

    const filterForms = document.querySelectorAll('.filter-form');

    filterForms.forEach(form => {
        form.addEventListener('reset', function(event) {
            event.preventDefault();
            const newUrl = new URL(window.location.href);
            newUrl.search = '';
            window.location.href = newUrl.href;
        });
    });    
}());


