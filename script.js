document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');

    searchForm.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission
        const query = document.getElementById('query').value;
        searchQuotes(query);
    });
});

function searchQuotes(query) {
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: query }),
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data.results);
    })
    .catch(error => {
        console.error('Error:', error);
        displayResults([]); // Display nothing or error message
    });
}

function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; // Clear previous results

    if (results.length === 0) {
        resultsDiv.innerHTML = '<p>No results found.</p>';
        return;
    }

    results.forEach(result => {
        const resultDiv = document.createElement('div');
        resultDiv.innerHTML = `
            <p><b>${result.author}</b></p>
            <p>${result.quote}</p>
            <p>Category: ${result.category}</p>
        `;
        resultsDiv.appendChild(resultDiv);
    });
}
