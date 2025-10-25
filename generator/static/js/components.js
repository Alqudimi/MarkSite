document.addEventListener('DOMContentLoaded', function() {
    initCopyButtons();
    initCodeCopyButtons();
    initCollapsibleAnimations();
});

function initCopyButtons() {
    const copyButtons = document.querySelectorAll('.copy-btn');
    
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const textToCopy = this.getAttribute('data-copy');
            
            if (textToCopy) {
                copyToClipboard(textToCopy, this);
            }
        });
    });
}

function initCodeCopyButtons() {
    const codeCopyButtons = document.querySelectorAll('.copy-code-btn');
    
    codeCopyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const codeId = this.getAttribute('data-code-id');
            const codeElement = document.getElementById(codeId);
            
            if (codeElement) {
                const codeToCopy = codeElement.textContent;
                copyToClipboard(codeToCopy, this);
            }
        });
    });
}

function copyToClipboard(text, button) {
    navigator.clipboard.writeText(text).then(function() {
        const originalHTML = button.innerHTML;
        button.innerHTML = '<i class="bi bi-check"></i> Copied!';
        button.classList.add('btn-success');
        
        setTimeout(function() {
            button.innerHTML = originalHTML;
            button.classList.remove('btn-success');
        }, 2000);
    }).catch(function(error) {
        console.error('Copy failed:', error);
        alert('Failed to copy to clipboard');
    });
}

function initCollapsibleAnimations() {
    const collapsibles = document.querySelectorAll('.collapsible-component .collapse');
    
    collapsibles.forEach(collapse => {
        collapse.addEventListener('show.bs.collapse', function() {
            const button = document.querySelector(`[data-bs-target="#${this.id}"]`);
            if (button) {
                button.querySelector('.bi-chevron-down').style.transform = 'rotate(180deg)';
            }
        });
        
        collapse.addEventListener('hide.bs.collapse', function() {
            const button = document.querySelector(`[data-bs-target="#${this.id}"]`);
            if (button) {
                button.querySelector('.bi-chevron-down').style.transform = 'rotate(0deg)';
            }
        });
    });
}

window.addEventListener('load', function() {
    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach((el, index) => {
        el.style.animationDelay = `${index * 0.1}s`;
    });
});
