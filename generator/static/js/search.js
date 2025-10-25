document.addEventListener('DOMContentLoaded', function() {
    let searchIndex = null;
    let lunrIndex = null;
    
    fetch('/static/js/search-index.json')
        .then(response => response.json())
        .then(data => {
            searchIndex = data;
            
            lunrIndex = lunr(function() {
                this.ref('url');
                this.field('title', { boost: 10 });
                this.field('description', { boost: 5 });
                this.field('content');
                
                data.forEach(doc => {
                    this.add(doc);
                });
            });
        })
        .catch(error => {
            console.error('Error loading search index:', error);
        });
    
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.trim();
            
            if (query.length < 2) {
                searchResults.innerHTML = '';
                return;
            }
            
            if (!lunrIndex || !searchIndex) {
                searchResults.innerHTML = '<p class="text-muted">Search index is loading...</p>';
                return;
            }
            
            try {
                const results = lunrIndex.search(query + '*');
                
                if (results.length === 0) {
                    searchResults.innerHTML = '<p class="text-muted">No results found</p>';
                    return;
                }
                
                const resultsHtml = results.slice(0, 10).map(result => {
                    const doc = searchIndex.find(d => d.url === result.ref);
                    if (!doc) return '';
                    
                    return `
                        <div class="search-result-item" onclick="window.location.href='${doc.url}'">
                            <h6 class="mb-1">${highlightMatch(doc.title, query)}</h6>
                            ${doc.description ? `<p class="text-muted small mb-1">${highlightMatch(doc.description, query)}</p>` : ''}
                            <small class="text-primary">${doc.url}</small>
                        </div>
                    `;
                }).join('');
                
                searchResults.innerHTML = resultsHtml;
            } catch (error) {
                console.error('Search error:', error);
                searchResults.innerHTML = '<p class="text-danger">Search error occurred</p>';
            }
        });
    }
    
    function highlightMatch(text, query) {
        if (!text) return '';
        const regex = new RegExp(`(${escapeRegex(query)})`, 'gi');
        return text.replace(regex, '<mark>$1</mark>');
    }
    
    function escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }
    
    const searchModal = document.getElementById('searchModal');
    if (searchModal) {
        searchModal.addEventListener('shown.bs.modal', function() {
            searchInput.focus();
        });
        
        searchModal.addEventListener('hidden.bs.modal', function() {
            searchInput.value = '';
            searchResults.innerHTML = '';
        });
    }
});
