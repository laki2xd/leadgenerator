let currentCompanies = [];
let currentSearchType = 'industry';
let currentSearchQuery = '';

// Search History Management - Server-side storage
async function getSearchHistory(searchType = null) {
    try {
        const url = searchType ? `/api/history?type=${searchType}` : '/api/history';
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Failed to fetch history');
        }
        const data = await response.json();
        return data.history || [];
    } catch (e) {
        console.error('Error reading search history:', e);
        return [];
    }
}

async function addToHistory(searchType, query, industryFilter = '') {
    try {
        const response = await fetch('/api/history', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                type: searchType,
                query: query.trim(),
                industry_filter: industryFilter.trim()
            })
        });
        
        if (!response.ok) {
            throw new Error('Failed to save history');
        }
        
        // Update history buttons after successful save
        await updateHistoryButtons();
    } catch (e) {
        console.error('Error saving search history:', e);
    }
}


// Clear history function kept for potential future use, but button removed
function clearHistory() {
    if (confirm('Are you sure you want to clear all search history?')) {
        saveSearchHistory([]);
        updateHistoryButtons();
        renderHistory();
    }
}

function formatDate(timestamp) {
    const date = new Date(timestamp);
    const now = new Date();
    const diffMs = now - date;
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMs / 3600000);
    const diffDays = Math.floor(diffMs / 86400000);
    
    if (diffMins < 1) return 'Just now';
    if (diffMins < 60) return `${diffMins}m ago`;
    if (diffHours < 24) return `${diffHours}h ago`;
    if (diffDays < 7) return `${diffDays}d ago`;
    
    return date.toLocaleDateString();
}

async function updateHistoryButtons() {
    try {
        const industryHistory = await getSearchHistory('industry');
        const productHistory = await getSearchHistory('product');
        
        const industryBtn = document.getElementById('industryHistoryBtn');
        const productBtn = document.getElementById('productHistoryBtn');
        
        if (industryBtn) {
            const count = industryHistory.length;
            const countBadge = industryBtn.querySelector('.history-count');
            if (count > 0) {
                if (!countBadge) {
                    const badge = document.createElement('span');
                    badge.className = 'history-count';
                    industryBtn.appendChild(badge);
                }
                industryBtn.querySelector('.history-count').textContent = count;
            } else if (countBadge) {
                countBadge.remove();
            }
        }
        
        if (productBtn) {
            const count = productHistory.length;
            const countBadge = productBtn.querySelector('.history-count');
            if (count > 0) {
                if (!countBadge) {
                    const badge = document.createElement('span');
                    badge.className = 'history-count';
                    productBtn.appendChild(badge);
                }
                productBtn.querySelector('.history-count').textContent = count;
            } else if (countBadge) {
                countBadge.remove();
            }
        }
    } catch (e) {
        console.error('Error updating history buttons:', e);
    }
}

async function renderHistory() {
    const historyList = document.getElementById('historyList');
    const currentType = currentSearchType;
    
    try {
        // Fetch history from server filtered by current type
        const filteredHistory = await getSearchHistory(currentType);
        
        if (filteredHistory.length === 0) {
            historyList.innerHTML = '<div class="history-empty">No search history yet</div>';
            return;
        }
    
        historyList.innerHTML = filteredHistory.map(item => {
            return `
            <div class="history-item" data-id="${item.id}">
                <div class="history-item-content">
                    <div class="history-item-query">${escapeHtml(item.query || '')}</div>
                    <div class="history-item-meta">
                        <span class="history-item-type">${item.type || 'unknown'}</span>
                        ${item.industry_filter ? `<span>Filter: ${escapeHtml(item.industry_filter)}</span>` : ''}
                        <span class="history-item-date">${formatDate(item.timestamp)}</span>
                    </div>
                </div>
            </div>
        `;
        }).join('');
        
        // Add click handlers to history items
        historyList.querySelectorAll('.history-item').forEach(item => {
            const itemId = parseInt(item.dataset.id);
            const historyItem = filteredHistory.find(h => h.id === itemId);
            
            // Item click handler (select from history)
            item.addEventListener('click', function(e) {
                if (historyItem) {
                    selectFromHistory(historyItem);
                    closeHistoryModal();
                }
            });
        });
    } catch (e) {
        console.error('Error rendering history:', e);
        historyList.innerHTML = '<div class="history-empty">Error loading history</div>';
    }
}

function selectFromHistory(historyItem) {
    if (historyItem.type === 'industry') {
        document.getElementById('industry').value = historyItem.query || '';
        // Switch to industry tab if not already
        if (currentSearchType !== 'industry') {
            document.querySelector('[data-tab="industry"]').click();
        }
    } else if (historyItem.type === 'product') {
        document.getElementById('product').value = historyItem.query || '';
        if (historyItem.industry_filter) {
            document.getElementById('productIndustry').value = historyItem.industry_filter;
        }
        // Switch to product tab if not already
        if (currentSearchType !== 'product') {
            document.querySelector('[data-tab="product"]').click();
        }
    }
    
    // Focus on the input
    const inputId = historyItem.type === 'industry' ? 'industry' : 'product';
    document.getElementById(inputId).focus();
}

function openHistoryModal() {
    const modal = document.getElementById('historyModal');
    renderHistory();
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeHistoryModal() {
    const modal = document.getElementById('historyModal');
    modal.classList.add('hidden');
    document.body.style.overflow = '';
}

// History modal event listeners
document.addEventListener('DOMContentLoaded', function() {
    const industryHistoryBtn = document.getElementById('industryHistoryBtn');
    const productHistoryBtn = document.getElementById('productHistoryBtn');
    const closeHistoryBtn = document.getElementById('closeHistoryModal');
    const historyModal = document.getElementById('historyModal');
    
    if (industryHistoryBtn) {
        industryHistoryBtn.addEventListener('click', function() {
            currentSearchType = 'industry';
            openHistoryModal();
        });
    }
    
    if (productHistoryBtn) {
        productHistoryBtn.addEventListener('click', function() {
            currentSearchType = 'product';
            openHistoryModal();
        });
    }
    
    if (closeHistoryBtn) {
        closeHistoryBtn.addEventListener('click', closeHistoryModal);
    }
    
    // Close modal when clicking outside
    if (historyModal) {
        historyModal.addEventListener('click', function(e) {
            if (e.target === historyModal) {
                closeHistoryModal();
            }
        });
    }
    
    // Close modal on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && !historyModal.classList.contains('hidden')) {
            closeHistoryModal();
        }
    });
    
    // Initialize history buttons on page load
    updateHistoryButtons();
    
    // Refresh history buttons periodically (every 30 seconds) to show updates from other users
    setInterval(updateHistoryButtons, 30000);
});

// Tab switching with smooth transitions
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        const tab = this.dataset.tab;
        currentSearchType = tab;
        
        // Update tab buttons
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        
        // Update tab content with fade transition
        document.querySelectorAll('.tab-content').forEach(c => {
            if (c.classList.contains('active')) {
                c.style.opacity = '0';
                setTimeout(() => {
                    c.classList.remove('active');
                }, 150);
            }
        });
        
        setTimeout(() => {
            const targetTab = document.getElementById(tab + 'Tab');
            targetTab.classList.add('active');
            targetTab.style.opacity = '0';
            setTimeout(() => {
                targetTab.style.opacity = '1';
            }, 10);
        }, 150);
        
        // Update history modal if it's open
        const historyModal = document.getElementById('historyModal');
        if (historyModal && !historyModal.classList.contains('hidden')) {
            renderHistory();
        }
    });
});

document.getElementById('searchBtn').addEventListener('click', searchCompanies);
document.getElementById('exportBtn').addEventListener('click', exportToExcel);

// Enter key handlers
document.getElementById('industry').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchCompanies();
    }
});

document.getElementById('product').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchCompanies();
    }
});

document.getElementById('productIndustry').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchCompanies();
    }
});

let progressInterval = null;

async function searchCompanies() {
    let searchQuery = '';
    let searchType = currentSearchType;
    
    if (searchType === 'industry') {
        searchQuery = document.getElementById('industry').value.trim();
        if (!searchQuery) {
            showError('Please enter an industry name');
            return;
        }
    } else {
        searchQuery = document.getElementById('product').value.trim();
        if (!searchQuery) {
            showError('Please enter a product/object name');
            return;
        }
    }
    
    // Show loading state
    const loadingEl = document.getElementById('loading');
    const errorEl = document.getElementById('error');
    const resultsEl = document.getElementById('results');
    const searchBtn = document.getElementById('searchBtn');
    
    loadingEl.classList.remove('hidden');
    errorEl.classList.add('hidden');
    resultsEl.classList.add('hidden');
    searchBtn.disabled = true;
    
    // Smooth scroll to loading section
    setTimeout(() => {
        loadingEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);
    
    // Clear previous progress
    const progressBox = document.getElementById('progressBox');
    if (progressBox) {
        progressBox.innerHTML = '';
    }
    
    // Start progress polling - reduced frequency to avoid overwhelming server
    progressInterval = setInterval(updateProgress, 1000); // Update every 1 second
    
    try {
        const requestBody = searchType === 'industry' 
            ? { industry: searchQuery, search_type: 'industry' }
            : { 
                product: searchQuery, 
                search_type: 'product',
                industry_filter: document.getElementById('productIndustry').value.trim() || ''
              };
        
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });
        
        // Check if response has content before parsing JSON
        const responseText = await response.text();
        if (!responseText || responseText.trim() === '') {
            throw new Error('Empty response from server. Please check Render logs for errors.');
        }
        
        let data;
        try {
            data = JSON.parse(responseText);
        } catch (parseError) {
            console.error('Failed to parse JSON response:', responseText);
            throw new Error('Invalid response from server. Please check Render logs. Response: ' + responseText.substring(0, 200));
        }
        
        // Stop progress polling
        if (progressInterval) {
            clearInterval(progressInterval);
            progressInterval = null;
        }
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to search companies');
        }
        
        if (data.error && data.companies.length < 10) {
            showError(data.error);
            if (data.companies.length > 0) {
                currentCompanies = data.companies;
                displayResults(data.companies, data.count);
            }
        } else {
            currentCompanies = data.companies;
            currentSearchQuery = searchQuery; // Store the search query for export
            
            // Save to search history (server-side)
            const industryFilter = searchType === 'product' 
                ? document.getElementById('productIndustry').value.trim() 
                : '';
            // Don't await - let it save in background
            addToHistory(searchType, searchQuery, industryFilter);
            
            displayResults(data.companies, data.count);
        }
        
    } catch (error) {
        if (progressInterval) {
            clearInterval(progressInterval);
            progressInterval = null;
        }
        showError('Error searching for companies: ' + error.message);
    } finally {
        document.getElementById('loading').classList.add('hidden');
        const searchBtn = document.getElementById('searchBtn');
        searchBtn.disabled = false;
    }
}

async function updateProgress() {
    try {
        const response = await fetch('/api/progress');
        if (!response.ok) {
            return; // Silently fail if there's an error
        }
        
        const progress = await response.json();
        
        const progressBox = document.getElementById('progressBox');
        if (!progressBox) return;
        
        // Update status
        const statusText = document.getElementById('progressStatus');
        if (statusText) {
            statusText.textContent = progress.current_step || progress.status || 'Searching...';
        }
        
        // Update companies count
        const countText = document.getElementById('progressCount');
        if (countText) {
            countText.textContent = progress.companies_found || 0;
        }
        
        // Update details log
        const detailsBox = document.getElementById('progressDetails');
        if (detailsBox && progress.details && progress.details.length > 0) {
            const recentDetails = progress.details.slice(-15); // Show last 15
            detailsBox.innerHTML = recentDetails.map(d => {
                const message = escapeHtml(d.message || '');
                let className = 'progress-detail';
                if (message.toLowerCase().includes('found:')) {
                    className += ' progress-found';
                } else if (message.toLowerCase().includes('error') || message.toLowerCase().includes('timeout')) {
                    className += ' progress-error';
                } else if (message.toLowerCase().includes('skipped')) {
                    className += ' progress-warning';
                }
                return `<div class="${className}">[${d.time || ''}] ${message}</div>`;
            }).join('');
            // Auto-scroll to bottom
            detailsBox.scrollTop = detailsBox.scrollHeight;
        }
        
        // Update progress bar if exists
        const progressBar = document.getElementById('progressBar');
        if (progressBar && progress.total_steps > 0) {
            const percent = Math.min(100, (progress.current_step_num / progress.total_steps) * 100);
            progressBar.style.width = percent + '%';
        } else if (progressBar && progress.companies_found > 0) {
            // Show some progress based on companies found (rough estimate)
            const estimatedPercent = Math.min(90, progress.companies_found * 2); // Rough estimate
            progressBar.style.width = estimatedPercent + '%';
        }
        
    } catch (error) {
        // Silently fail - progress is optional, don't spam console
        console.debug('Progress update failed:', error);
    }
}

function displayResults(companies, count) {
    document.getElementById('count').textContent = count;
    const resultsEl = document.getElementById('results');
    resultsEl.classList.remove('hidden');
    
    const companiesList = document.getElementById('companiesList');
    companiesList.innerHTML = '';
    
    // Smooth scroll to results
    setTimeout(() => {
        resultsEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);
    
    companies.forEach((company, index) => {
        const card = document.createElement('div');
        card.className = 'company-card';
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        const countryClass = company.country === 'Canada' ? 'country-canada' : 'country-usa';
        
        card.innerHTML = `
            <div class="company-name">${escapeHtml(company.name)}</div>
            <div class="company-detail"><strong>Industry:</strong> ${escapeHtml(company.industry)}</div>
            ${company.business_type ? `<div class="company-detail"><strong>Type:</strong> ${escapeHtml(company.business_type)}</div>` : ''}
            <div class="company-detail"><strong>Address:</strong> ${escapeHtml(company.address || 'N/A')}</div>
            ${company.phone ? `<div class="company-detail"><strong>Phone:</strong> <a href="tel:${escapeHtml(company.phone)}">${escapeHtml(company.phone)}</a></div>` : ''}
            ${company.email ? `<div class="company-detail"><strong>Email:</strong> <a href="mailto:${escapeHtml(company.email)}">${escapeHtml(company.email)}</a></div>` : ''}
            ${company.website ? `<div class="company-detail"><strong>Website:</strong> <a href="${escapeHtml(company.website)}" target="_blank">Visit</a></div>` : ''}
            ${company.rating ? `<div class="company-detail"><strong>Rating:</strong> ${company.rating}/5</div>` : ''}
            <span class="country-badge ${countryClass}">${escapeHtml(company.country)}</span>
        `;
        
        companiesList.appendChild(card);
        
        // Staggered fade-in animation
        setTimeout(() => {
            card.style.transition = 'opacity 0.4s ease-out, transform 0.4s ease-out';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 30);
    });
}

async function exportToExcel() {
    if (currentCompanies.length === 0) {
        showError('No companies to export. Please search for companies first.');
        return;
    }
    
    const exportBtn = document.getElementById('exportBtn');
    const btnText = exportBtn.querySelector('.btn-text');
    const btnIcon = exportBtn.querySelector('.btn-icon');
    
    exportBtn.disabled = true;
    if (btnText) {
        btnText.textContent = 'Exporting...';
    }
    
    try {
        const response = await fetch('/api/export', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                companies: currentCompanies,
                search_query: currentSearchQuery || 'companies'
            })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Failed to export');
        }
        
        // Download the file
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        // Get filename from Content-Disposition header or use default
        const contentDisposition = response.headers.get('Content-Disposition');
        let downloadFilename = `companies_${new Date().toISOString().split('T')[0]}.xlsx`;
        if (contentDisposition) {
            const filenameMatch = contentDisposition.match(/filename="(.+)"/);
            if (filenameMatch) {
                downloadFilename = filenameMatch[1];
            }
        }
        a.download = downloadFilename;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
        
        // Show success message
        showSuccess('Excel file downloaded successfully!');
        
    } catch (error) {
        showError('Error exporting to Excel: ' + error.message);
    } finally {
        exportBtn.disabled = false;
        if (btnText) {
            btnText.textContent = 'Export to Excel';
        }
        if (btnIcon) {
            btnIcon.textContent = '📥';
        }
    }
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.className = 'alert alert-error';
    errorDiv.classList.remove('hidden');
    
    // Smooth scroll to error
    setTimeout(() => {
        errorDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);
}

function showSuccess(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.className = 'alert alert-success';
    errorDiv.classList.remove('hidden');
    
    // Smooth scroll to success message
    setTimeout(() => {
        errorDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);
    
    setTimeout(() => {
        errorDiv.classList.add('hidden');
    }, 4000);
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

