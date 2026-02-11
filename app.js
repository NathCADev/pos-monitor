/**
 * Application JavaScript
 * Monitor de Pós-Graduação EAD
 * 
 * Estrutura:
 * 1. State Management
 * 2. Data Fetching
 * 3. UI Rendering
 * 4. Filters & Search
 * 5. Utilities
 * 6. Initialization
 */

/* ============================================
   1. STATE MANAGEMENT
   ============================================ */
const AppState = {
  data: null,
  filteredData: null,
  currentFilters: {
    instituto: '',
    searchTerm: ''
  }
};

/* ============================================
   2. DATA FETCHING
   ============================================ */

/**
 * Carrega os dados do arquivo JSON gerado pelo GitHub Actions
 * @returns {Promise<Object>} Dados das oportunidades
 */
async function fetchData() {
  try {
    const response = await fetch('resultados.json');
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
    
  } catch (error) {
    console.error('Erro ao carregar dados:', error);
    showError('Não foi possível carregar os dados. Tente novamente mais tarde.');
    return null;
  }
}

/**
 * Inicializa a aplicação carregando e renderizando os dados
 */
async function initializeApp() {
  // Mostra loading state
  showLoading();
  
  // Carrega dados
  const data = await fetchData();
  
  if (!data) {
    hideLoading();
    return;
  }
  
  // Atualiza state
  AppState.data = data;
  AppState.filteredData = data.oportunidades;
  
  // Renderiza UI
  hideLoading();
  renderStatusBar(data);
  populateFilters(data);
  renderOpportunities(AppState.filteredData);
  renderStatistics(data);
}

/* ============================================
   3. UI RENDERING
   ============================================ */

/**
 * Renderiza a barra de status com informações gerais
 * @param {Object} data - Dados completos
 */
function renderStatusBar(data) {
  const lastUpdateElement = document.getElementById('lastUpdate');
  const totalCountElement = document.getElementById('totalCount');
  
  if (lastUpdateElement) {
    lastUpdateElement.textContent = formatDateTime(data.ultima_atualizacao);
  }
  
  if (totalCountElement) {
    totalCountElement.textContent = data.total_oportunidades;
  }
}

/**
 * Renderiza os cards de oportunidades
 * @param {Array} opportunities - Lista de oportunidades
 */
function renderOpportunities(opportunities) {
  const grid = document.getElementById('opportunitiesGrid');
  const emptyState = document.getElementById('emptyState');
  
  if (!grid) return;
  
  // Limpa o grid
  grid.innerHTML = '';
  
  // Verifica se há oportunidades
  if (!opportunities || opportunities.length === 0) {
    grid.style.display = 'none';
    if (emptyState) emptyState.style.display = 'block';
    return;
  }
  
  grid.style.display = 'grid';
  if (emptyState) emptyState.style.display = 'none';
  
  // Renderiza cada card
  opportunities.forEach(oport => {
    const card = createOpportunityCard(oport);
    grid.appendChild(card);
  });
}

/**
 * Cria um card de oportunidade
 * @param {Object} oport - Dados da oportunidade
 * @returns {HTMLElement} Elemento do card
 */
function createOpportunityCard(oport) {
  const card = document.createElement('article');
  card.className = 'card';
  
  card.innerHTML = `
    <div class="card__header">
      <div class="card__icon">
        <i class="fa-solid fa-building-columns"></i>
      </div>
      <div class="card__instituto">${escapeHtml(oport.instituto)}</div>
    </div>
    
    <h3 class="card__title">${escapeHtml(oport.titulo)}</h3>
    
    <div class="card__meta">
      <i class="fa-regular fa-calendar"></i>
      <span>Encontrado ${formatRelativeTime(oport.data_encontrado)}</span>
    </div>
    
    <a href="${escapeHtml(oport.url)}" 
       target="_blank" 
       rel="noopener noreferrer" 
       class="card__link">
      Ver edital completo
      <i class="fa-solid fa-arrow-right"></i>
    </a>
  `;
  
  return card;
}

/**
 * Renderiza as estatísticas
 * @param {Object} data - Dados completos
 */
function renderStatistics(data) {
  const section = document.getElementById('statisticsSection');
  const grid = document.getElementById('statisticsGrid');
  
  if (!grid || !data.estatisticas) return;
  
  grid.innerHTML = '';
  
  // Ordena institutos por quantidade
  const institutos = Object.entries(data.estatisticas.por_instituto)
    .sort((a, b) => b[1] - a[1]);
  
  // Renderiza cards de estatísticas
  institutos.forEach(([instituto, count]) => {
    const statCard = document.createElement('div');
    statCard.className = 'stat-card';
    
    statCard.innerHTML = `
      <div class="stat-card__label">${escapeHtml(instituto)}</div>
      <div class="stat-card__value">${count}</div>
    `;
    
    grid.appendChild(statCard);
  });
  
  if (section) {
    section.style.display = 'block';
  }
}

/**
 * Popula os filtros com opções disponíveis
 * @param {Object} data - Dados completos
 */
function populateFilters(data) {
  const selectInstituto = document.getElementById('filterInstituto');
  
  if (!selectInstituto || !data.institutos_unicos) return;
  
  // Adiciona opções de institutos
  data.institutos_unicos.sort().forEach(instituto => {
    const option = document.createElement('option');
    option.value = instituto;
    option.textContent = instituto;
    selectInstituto.appendChild(option);
  });
}

/* ============================================
   4. FILTERS & SEARCH
   ============================================ */

/**
 * Aplica os filtros às oportunidades
 */
function applyFilters() {
  if (!AppState.data) return;
  
  let filtered = AppState.data.oportunidades;
  
  // Filtro por instituto
  if (AppState.currentFilters.instituto) {
    filtered = filtered.filter(oport => 
      oport.instituto === AppState.currentFilters.instituto
    );
  }
  
  // Filtro por termo de busca
  if (AppState.currentFilters.searchTerm) {
    const term = AppState.currentFilters.searchTerm.toLowerCase();
    filtered = filtered.filter(oport => 
      oport.titulo.toLowerCase().includes(term) ||
      oport.instituto.toLowerCase().includes(term)
    );
  }
  
  AppState.filteredData = filtered;
  renderOpportunities(filtered);
}

/**
 * Configura os event listeners dos filtros
 */
function setupFilters() {
  const filterInstituto = document.getElementById('filterInstituto');
  const searchTerm = document.getElementById('searchTerm');
  
  if (filterInstituto) {
    filterInstituto.addEventListener('change', (e) => {
      AppState.currentFilters.instituto = e.target.value;
      applyFilters();
    });
  }
  
  if (searchTerm) {
    // Debounce para evitar muitas renderizações
    let timeout;
    searchTerm.addEventListener('input', (e) => {
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        AppState.currentFilters.searchTerm = e.target.value;
        applyFilters();
      }, 300);
    });
  }
}

/* ============================================
   5. UTILITIES
   ============================================ */

/**
 * Formata uma data ISO para formato brasileiro com horário
 * @param {string} isoString - Data em formato ISO
 * @returns {string} Data formatada
 */
function formatDateTime(isoString) {
  const date = new Date(isoString);
  
  const options = {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  };
  
  return date.toLocaleString('pt-BR', options);
}

/**
 * Formata uma data como tempo relativo (ex: "há 2 horas")
 * @param {string} isoString - Data em formato ISO
 * @returns {string} Tempo relativo formatado
 */
function formatRelativeTime(isoString) {
  const date = new Date(isoString);
  const now = new Date();
  const diffMs = now - date;
  const diffMins = Math.floor(diffMs / 60000);
  const diffHours = Math.floor(diffMins / 60);
  const diffDays = Math.floor(diffHours / 24);
  
  if (diffMins < 1) return 'agora mesmo';
  if (diffMins < 60) return `há ${diffMins} minuto${diffMins > 1 ? 's' : ''}`;
  if (diffHours < 24) return `há ${diffHours} hora${diffHours > 1 ? 's' : ''}`;
  if (diffDays < 7) return `há ${diffDays} dia${diffDays > 1 ? 's' : ''}`;
  
  // Mais de uma semana, mostra a data completa
  return formatDateTime(isoString);
}

/**
 * Escapa HTML para prevenir XSS
 * @param {string} text - Texto para escapar
 * @returns {string} Texto escapado
 */
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

/**
 * Mostra o estado de loading
 */
function showLoading() {
  const loading = document.getElementById('loadingState');
  const grid = document.getElementById('opportunitiesGrid');
  const empty = document.getElementById('emptyState');
  
  if (loading) loading.style.display = 'grid';
  if (grid) grid.style.display = 'none';
  if (empty) empty.style.display = 'none';
}

/**
 * Esconde o estado de loading
 */
function hideLoading() {
  const loading = document.getElementById('loadingState');
  if (loading) loading.style.display = 'none';
}

/**
 * Mostra uma mensagem de erro
 * @param {string} message - Mensagem de erro
 */
function showError(message) {
  const grid = document.getElementById('opportunitiesGrid');
  if (!grid) return;
  
  grid.innerHTML = `
    <div class="empty-state" style="display: block; grid-column: 1 / -1;">
      <i class="fa-solid fa-triangle-exclamation empty-state__icon" style="color: var(--color-error);"></i>
      <h2 class="empty-state__title">Erro ao carregar dados</h2>
      <p class="empty-state__text">${escapeHtml(message)}</p>
    </div>
  `;
}

/* ============================================
   6. INITIALIZATION
   ============================================ */

/**
 * Inicializa a aplicação quando o DOM estiver pronto
 */
document.addEventListener('DOMContentLoaded', () => {
  setupFilters();
  initializeApp();
});

/**
 * Auto-refresh a cada 5 minutos para pegar novos dados
 * (caso o GitHub Actions tenha atualizado o JSON)
 */
setInterval(() => {
  console.log('Verificando atualizações...');
  initializeApp();
}, 5 * 60 * 1000); // 5 minutos
