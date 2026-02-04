import React, { useState } from 'react';
import { TrendingUp, Package, DollarSign, Users, Calendar, Target, Database, GitBranch, History, Download, Settings, Filter, ChevronDown, ChevronRight, BarChart3, Layers, AlertCircle, Check, X, Edit2, Save } from 'lucide-react';

const SandozPipelinePlatform = () => {
  const [selectedProduct, setSelectedProduct] = useState('PRODUCT-001');
  const [activeTab, setActiveTab] = useState('assumptions');
  const [viewMode, setViewMode] = useState('single'); // 'single' or 'portfolio'
  const [showVersionHistory, setShowVersionHistory] = useState(false);
  const [editingAssumption, setEditingAssumption] = useState(null);
  const [showScenarioComparison, setShowScenarioComparison] = useState(false);

  // Sample pipeline products
  const pipelineProducts = [
    {
      id: 'PRODUCT-001',
      name: 'Biosimilar Humira (Adalimumab)',
      archetype: 'Med Benefit High',
      phase: 'Pre-Launch',
      launchDate: '2026-Q2',
      territory: 'US',
      priority: 'High',
      npv: 245.6,
      assumptions: {
        uptake: { y1: 8, y2: 15, y3: 22, y4: 28, y5: 32 },
        peakShare: 32,
        pricing: { wac: 850, asp: 765, gtn: 45 },
        access: { tier1: 60, tier2: 30, tier3: 10 },
        competition: 'High (5+ competitors)',
        jcode: 'Applied - 18mo to launch',
        distribution: 'Specialty + Limited'
      },
      lastUpdated: '2026-01-28',
      updatedBy: 'Sarah Chen (US Market Access)'
    },
    {
      id: 'PRODUCT-002',
      name: 'Biosimilar Enbrel (Etanercept)',
      archetype: 'Med Benefit Med',
      phase: 'Filed',
      launchDate: '2026-Q4',
      territory: 'US',
      priority: 'Medium',
      npv: 178.3,
      assumptions: {
        uptake: { y1: 6, y2: 12, y3: 18, y4: 24, y5: 28 },
        peakShare: 28,
        pricing: { wac: 720, asp: 648, gtn: 42 },
        access: { tier1: 55, tier2: 35, tier3: 10 },
        competition: 'Medium (3-4 competitors)',
        jcode: 'Pending - 24mo to launch',
        distribution: 'Specialty'
      },
      lastUpdated: '2026-01-25',
      updatedBy: 'Michael Torres (Global BD)'
    },
    {
      id: 'PRODUCT-003',
      name: 'Generic Lyrica (Pregabalin)',
      archetype: 'Rx Benefit High',
      phase: 'Pre-Launch',
      launchDate: '2026-Q3',
      territory: 'US',
      priority: 'High',
      npv: 189.4,
      assumptions: {
        uptake: { y1: 25, y2: 38, y3: 45, y4: 48, y5: 50 },
        peakShare: 50,
        pricing: { wac: 45, asp: 38, gtn: 65 },
        access: { tier1: 85, tier2: 12, tier3: 3 },
        competition: 'High (10+ competitors)',
        jcode: 'N/A - Retail',
        distribution: 'Retail + Specialty'
      },
      lastUpdated: '2026-01-27',
      updatedBy: 'Jennifer Liu (US Market Access)'
    },
    {
      id: 'PRODUCT-004',
      name: 'Rare Disease Gene Therapy',
      archetype: 'Rare Disease',
      phase: 'Phase 3',
      launchDate: '2027-Q2',
      territory: 'US',
      priority: 'Strategic',
      npv: 312.8,
      assumptions: {
        uptake: { y1: 3, y2: 6, y3: 9, y4: 12, y5: 15 },
        peakShare: 15,
        pricing: { wac: 125000, asp: 115000, gtn: 28 },
        access: { tier1: 40, tier2: 35, tier3: 25 },
        competition: 'Low (1-2 competitors)',
        jcode: 'To be applied - 36mo to launch',
        distribution: 'Ultra-Specialty + Hub'
      },
      lastUpdated: '2026-01-20',
      updatedBy: 'David Park (Global Rare Disease)'
    }
  ];

  const [products, setProducts] = useState(pipelineProducts);
  const currentProduct = products.find(p => p.id === selectedProduct);

  // Version history for selected product
  const versionHistory = [
    {
      version: 'v1.3',
      date: '2026-01-28',
      user: 'Sarah Chen',
      changes: ['Updated GTN% from 42% to 45%', 'Revised Tier 1 access from 55% to 60%'],
      npvImpact: +12.3,
      status: 'Current'
    },
    {
      version: 'v1.2',
      date: '2026-01-15',
      user: 'Michael Torres',
      changes: ['Adjusted Y1 uptake from 6% to 8%', 'Updated competition assessment'],
      npvImpact: +8.7,
      status: 'Approved'
    },
    {
      version: 'v1.1',
      date: '2025-12-20',
      user: 'Jennifer Liu',
      changes: ['Initial US market assumptions', 'Added J-code timeline'],
      npvImpact: +15.2,
      status: 'Approved'
    },
    {
      version: 'v1.0',
      date: '2025-12-01',
      user: 'David Park',
      changes: ['Created baseline forecast from Global assumptions'],
      npvImpact: 0,
      status: 'Baseline'
    }
  ];

  const archetypes = [
    { name: 'Med Benefit High', color: '#0066CC', count: 8 },
    { name: 'Med Benefit Med', color: '#4A90E2', count: 6 },
    { name: 'Med Benefit Low', color: '#7AB8FF', count: 4 },
    { name: 'Rx Benefit High', color: '#00A86B', count: 7 },
    { name: 'Rx Benefit Med', color: '#52C993', count: 5 },
    { name: 'Rx Benefit Low', color: '#8FE5B8', count: 3 },
    { name: 'Rare Disease', color: '#9B59B6', count: 2 }
  ];

  // Portfolio summary calculations
  const portfolioNPV = products.reduce((sum, p) => sum + p.npv, 0);
  const highPriorityCount = products.filter(p => p.priority === 'High' || p.priority === 'Strategic').length;

  const getPriorityColor = (priority) => {
    const colors = {
      'High': '#E74C3C',
      'Strategic': '#9B59B6',
      'Medium': '#F39C12',
      'Low': '#95A5A6'
    };
    return colors[priority] || '#95A5A6';
  };

  const getArchetypeColor = (archetype) => {
    const type = archetypes.find(a => a.name === archetype);
    return type?.color || '#95A5A6';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 p-6">
      {/* Header */}
      <div className="mb-6 bg-white rounded-lg shadow-lg p-6 border-t-4" style={{ borderColor: '#2B5797' }}>
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <div className="bg-gradient-to-br from-blue-600 to-blue-700 p-3 rounded-lg">
              <Layers className="w-8 h-8 text-white" />
            </div>
            <div>
              <h1 className="text-3xl font-bold text-gray-800">Pipeline Decision System</h1>
              <p className="text-gray-600 mt-1">Centralized Portfolio Management & NPV Tracking</p>
            </div>
          </div>
          <div className="flex items-center space-x-2">
            <img src="/api/placeholder/120/40" alt="SANDOZ" className="h-8" style={{ filter: 'hue-rotate(200deg)' }} />
          </div>
        </div>

        {/* View Mode Toggle */}
        <div className="mt-4 flex items-center space-x-4">
          <button
            onClick={() => setViewMode('single')}
            className={`px-4 py-2 rounded-lg font-medium transition-all ${
              viewMode === 'single'
                ? 'bg-blue-600 text-white shadow-md'
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            <Package className="w-4 h-4 inline mr-2" />
            Single Product View
          </button>
          <button
            onClick={() => setViewMode('portfolio')}
            className={`px-4 py-2 rounded-lg font-medium transition-all ${
              viewMode === 'portfolio'
                ? 'bg-blue-600 text-white shadow-md'
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            <BarChart3 className="w-4 h-4 inline mr-2" />
            Portfolio View
          </button>
        </div>
      </div>

      {viewMode === 'portfolio' ? (
        /* PORTFOLIO VIEW */
        <div className="space-y-6">
          {/* Portfolio Summary Cards */}
          <div className="grid grid-cols-4 gap-4">
            <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-blue-600">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-gray-600 mb-1">Total Pipeline NPV</p>
                  <p className="text-3xl font-bold text-gray-800">${portfolioNPV.toFixed(1)}M</p>
                </div>
                <DollarSign className="w-10 h-10 text-blue-600 opacity-20" />
              </div>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-purple-600">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-gray-600 mb-1">Products in Pipeline</p>
                  <p className="text-3xl font-bold text-gray-800">{products.length}</p>
                </div>
                <Package className="w-10 h-10 text-purple-600 opacity-20" />
              </div>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-red-600">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-gray-600 mb-1">High Priority Assets</p>
                  <p className="text-3xl font-bold text-gray-800">{highPriorityCount}</p>
                </div>
                <Target className="w-10 h-10 text-red-600 opacity-20" />
              </div>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-md border-l-4 border-green-600">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-gray-600 mb-1">Launches This Year</p>
                  <p className="text-3xl font-bold text-gray-800">3</p>
                </div>
                <Calendar className="w-10 h-10 text-green-600 opacity-20" />
              </div>
            </div>
          </div>

          {/* Archetype Distribution */}
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center">
              <Filter className="w-5 h-5 mr-2 text-blue-600" />
              Portfolio by Archetype
            </h3>
            <div className="grid grid-cols-7 gap-4">
              {archetypes.map(archetype => (
                <div
                  key={archetype.name}
                  className="text-center p-4 rounded-lg border-2 hover:shadow-md transition-all cursor-pointer"
                  style={{ borderColor: archetype.color }}
                >
                  <div
                    className="w-16 h-16 rounded-full mx-auto mb-2 flex items-center justify-center text-white text-2xl font-bold"
                    style={{ backgroundColor: archetype.color }}
                  >
                    {archetype.count}
                  </div>
                  <p className="text-xs text-gray-600 font-medium">{archetype.name}</p>
                </div>
              ))}
            </div>
          </div>

          {/* Portfolio Table */}
          <div className="bg-white rounded-lg shadow-md overflow-hidden">
            <div className="p-6 border-b border-gray-200">
              <h3 className="text-lg font-bold text-gray-800 flex items-center">
                <Database className="w-5 h-5 mr-2 text-blue-600" />
                Pipeline Portfolio Overview
              </h3>
            </div>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Product</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Archetype</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Phase</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Launch</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Priority</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">NPV</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Last Updated</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {products.map(product => (
                    <tr key={product.id} className="hover:bg-gray-50">
                      <td className="px-6 py-4">
                        <div className="text-sm font-medium text-gray-900">{product.name}</div>
                        <div className="text-xs text-gray-500">{product.id}</div>
                      </td>
                      <td className="px-6 py-4">
                        <span
                          className="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full text-white"
                          style={{ backgroundColor: getArchetypeColor(product.archetype) }}
                        >
                          {product.archetype}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-900">{product.phase}</td>
                      <td className="px-6 py-4 text-sm text-gray-900">{product.launchDate}</td>
                      <td className="px-6 py-4">
                        <span
                          className="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full text-white"
                          style={{ backgroundColor: getPriorityColor(product.priority) }}
                        >
                          {product.priority}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-sm font-bold" style={{ color: '#2B5797' }}>
                        ${product.npv}M
                      </td>
                      <td className="px-6 py-4">
                        <div className="text-sm text-gray-900">{product.lastUpdated}</div>
                        <div className="text-xs text-gray-500">{product.updatedBy}</div>
                      </td>
                      <td className="px-6 py-4">
                        <button
                          onClick={() => {
                            setSelectedProduct(product.id);
                            setViewMode('single');
                          }}
                          className="text-blue-600 hover:text-blue-800 font-medium text-sm"
                        >
                          View Details →
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      ) : (
        /* SINGLE PRODUCT VIEW */
        <div className="grid grid-cols-12 gap-6">
          {/* Left Sidebar - Product Selector */}
          <div className="col-span-3 space-y-4">
            <div className="bg-white rounded-lg shadow-md p-4">
              <h3 className="text-sm font-bold text-gray-700 mb-3 flex items-center">
                <Package className="w-4 h-4 mr-2" />
                Pipeline Products
              </h3>
              <div className="space-y-2">
                {products.map(product => (
                  <button
                    key={product.id}
                    onClick={() => setSelectedProduct(product.id)}
                    className={`w-full text-left p-3 rounded-lg transition-all ${
                      selectedProduct === product.id
                        ? 'bg-blue-50 border-2 border-blue-600'
                        : 'bg-gray-50 border-2 border-transparent hover:bg-gray-100'
                    }`}
                  >
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <p className="text-sm font-medium text-gray-900">{product.name}</p>
                        <p className="text-xs text-gray-500 mt-1">{product.phase}</p>
                      </div>
                      {selectedProduct === product.id && (
                        <Check className="w-4 h-4 text-blue-600 flex-shrink-0 ml-2" />
                      )}
                    </div>
                    <div className="mt-2 flex items-center justify-between">
                      <span
                        className="text-xs px-2 py-0.5 rounded text-white"
                        style={{ backgroundColor: getArchetypeColor(product.archetype) }}
                      >
                        {product.archetype}
                      </span>
                      <span className="text-xs font-bold" style={{ color: '#2B5797' }}>
                        ${product.npv}M
                      </span>
                    </div>
                  </button>
                ))}
              </div>
            </div>

            {/* Quick Actions */}
            <div className="bg-white rounded-lg shadow-md p-4">
              <h3 className="text-sm font-bold text-gray-700 mb-3">Quick Actions</h3>
              <div className="space-y-2">
                <button
                  onClick={() => setShowVersionHistory(!showVersionHistory)}
                  className="w-full flex items-center justify-between p-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg"
                >
                  <span className="flex items-center">
                    <History className="w-4 h-4 mr-2" />
                    Version History
                  </span>
                  {showVersionHistory ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
                </button>
                <button
                  onClick={() => setShowScenarioComparison(!showScenarioComparison)}
                  className="w-full flex items-center justify-between p-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg"
                >
                  <span className="flex items-center">
                    <GitBranch className="w-4 h-4 mr-2" />
                    Compare Scenarios
                  </span>
                </button>
                <button className="w-full flex items-center p-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg">
                  <Download className="w-4 h-4 mr-2" />
                  Export to Excel
                </button>
              </div>
            </div>
          </div>

          {/* Main Content Area */}
          <div className="col-span-9 space-y-6">
            {/* Product Header Card */}
            <div className="bg-white rounded-lg shadow-md p-6">
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <h2 className="text-2xl font-bold text-gray-800">{currentProduct?.name}</h2>
                  <p className="text-gray-600 mt-1">{currentProduct?.id}</p>
                  <div className="flex items-center space-x-4 mt-3">
                    <span
                      className="px-3 py-1 text-sm font-semibold rounded-full text-white"
                      style={{ backgroundColor: getArchetypeColor(currentProduct?.archetype) }}
                    >
                      {currentProduct?.archetype}
                    </span>
                    <span
                      className="px-3 py-1 text-sm font-semibold rounded-full text-white"
                      style={{ backgroundColor: getPriorityColor(currentProduct?.priority) }}
                    >
                      {currentProduct?.priority} Priority
                    </span>
                    <span className="px-3 py-1 text-sm font-semibold rounded-full bg-gray-100 text-gray-700">
                      {currentProduct?.phase}
                    </span>
                  </div>
                </div>
                <div className="text-right">
                  <p className="text-sm text-gray-600">Net Present Value</p>
                  <p className="text-4xl font-bold mt-1" style={{ color: '#2B5797' }}>
                    ${currentProduct?.npv}M
                  </p>
                  <p className="text-xs text-gray-500 mt-2">
                    Launch: {currentProduct?.launchDate}
                  </p>
                </div>
              </div>
            </div>

            {/* Tabs */}
            <div className="bg-white rounded-lg shadow-md">
              <div className="border-b border-gray-200">
                <div className="flex space-x-1 p-2">
                  {['assumptions', 'financials', 'access', 'timeline'].map(tab => (
                    <button
                      key={tab}
                      onClick={() => setActiveTab(tab)}
                      className={`px-4 py-2 text-sm font-medium rounded-lg transition-all ${
                        activeTab === tab
                          ? 'bg-blue-600 text-white'
                          : 'text-gray-600 hover:bg-gray-100'
                      }`}
                    >
                      {tab.charAt(0).toUpperCase() + tab.slice(1)}
                    </button>
                  ))}
                </div>
              </div>

              <div className="p-6">
                {activeTab === 'assumptions' && (
                  <div className="space-y-6">
                    {/* Uptake Assumptions */}
                    <div>
                      <h4 className="text-lg font-bold text-gray-800 mb-4 flex items-center">
                        <TrendingUp className="w-5 h-5 mr-2 text-blue-600" />
                        Market Uptake Assumptions
                      </h4>
                      <div className="grid grid-cols-5 gap-4">
                        {Object.entries(currentProduct?.assumptions.uptake || {}).map(([year, value]) => (
                          <div key={year} className="bg-blue-50 p-4 rounded-lg border border-blue-200">
                            <p className="text-xs text-gray-600 mb-1">Year {year.replace('y', '')}</p>
                            <p className="text-2xl font-bold text-blue-600">{value}%</p>
                          </div>
                        ))}
                      </div>
                      <div className="mt-4 bg-gray-50 p-4 rounded-lg">
                        <div className="flex items-center justify-between">
                          <span className="text-sm font-medium text-gray-700">Peak Market Share</span>
                          <span className="text-xl font-bold text-blue-600">{currentProduct?.assumptions.peakShare}%</span>
                        </div>
                      </div>
                    </div>

                    {/* Pricing Assumptions */}
                    <div>
                      <h4 className="text-lg font-bold text-gray-800 mb-4 flex items-center">
                        <DollarSign className="w-5 h-5 mr-2 text-green-600" />
                        Pricing & GTN Assumptions
                      </h4>
                      <div className="grid grid-cols-3 gap-4">
                        <div className="bg-green-50 p-4 rounded-lg border border-green-200">
                          <p className="text-xs text-gray-600 mb-1">WAC (List Price)</p>
                          <p className="text-2xl font-bold text-green-600">
                            ${currentProduct?.assumptions.pricing.wac}
                          </p>
                        </div>
                        <div className="bg-green-50 p-4 rounded-lg border border-green-200">
                          <p className="text-xs text-gray-600 mb-1">ASP (Avg Sales Price)</p>
                          <p className="text-2xl font-bold text-green-600">
                            ${currentProduct?.assumptions.pricing.asp}
                          </p>
                        </div>
                        <div className="bg-green-50 p-4 rounded-lg border border-green-200">
                          <p className="text-xs text-gray-600 mb-1">Gross-to-Net %</p>
                          <p className="text-2xl font-bold text-green-600">
                            {currentProduct?.assumptions.pricing.gtn}%
                          </p>
                        </div>
                      </div>
                    </div>

                    {/* Access & Distribution */}
                    <div>
                      <h4 className="text-lg font-bold text-gray-800 mb-4 flex items-center">
                        <Target className="w-5 h-5 mr-2 text-purple-600" />
                        Access & Distribution
                      </h4>
                      <div className="grid grid-cols-2 gap-4">
                        <div className="bg-white p-4 rounded-lg border border-gray-200">
                          <p className="text-sm font-medium text-gray-700 mb-3">Formulary Coverage</p>
                          <div className="space-y-2">
                            <div className="flex items-center justify-between">
                              <span className="text-sm text-gray-600">Tier 1 (Preferred)</span>
                              <span className="font-bold text-purple-600">{currentProduct?.assumptions.access.tier1}%</span>
                            </div>
                            <div className="w-full bg-gray-200 rounded-full h-2">
                              <div className="bg-purple-600 h-2 rounded-full" style={{ width: `${currentProduct?.assumptions.access.tier1}%` }}></div>
                            </div>
                            <div className="flex items-center justify-between">
                              <span className="text-sm text-gray-600">Tier 2 (Non-Preferred)</span>
                              <span className="font-bold text-purple-400">{currentProduct?.assumptions.access.tier2}%</span>
                            </div>
                            <div className="w-full bg-gray-200 rounded-full h-2">
                              <div className="bg-purple-400 h-2 rounded-full" style={{ width: `${currentProduct?.assumptions.access.tier2}%` }}></div>
                            </div>
                            <div className="flex items-center justify-between">
                              <span className="text-sm text-gray-600">Tier 3 (Specialty)</span>
                              <span className="font-bold text-purple-300">{currentProduct?.assumptions.access.tier3}%</span>
                            </div>
                            <div className="w-full bg-gray-200 rounded-full h-2">
                              <div className="bg-purple-300 h-2 rounded-full" style={{ width: `${currentProduct?.assumptions.access.tier3}%` }}></div>
                            </div>
                          </div>
                        </div>
                        <div className="space-y-4">
                          <div className="bg-white p-4 rounded-lg border border-gray-200">
                            <p className="text-sm font-medium text-gray-700 mb-2">Competition Level</p>
                            <p className="text-lg font-bold text-gray-800">{currentProduct?.assumptions.competition}</p>
                          </div>
                          <div className="bg-white p-4 rounded-lg border border-gray-200">
                            <p className="text-sm font-medium text-gray-700 mb-2">J-Code Status</p>
                            <p className="text-lg font-bold text-gray-800">{currentProduct?.assumptions.jcode}</p>
                          </div>
                          <div className="bg-white p-4 rounded-lg border border-gray-200">
                            <p className="text-sm font-medium text-gray-700 mb-2">Distribution Channel</p>
                            <p className="text-lg font-bold text-gray-800">{currentProduct?.assumptions.distribution}</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {activeTab === 'financials' && (
                  <div className="space-y-6">
                    <div className="grid grid-cols-3 gap-4">
                      <div className="bg-gradient-to-br from-blue-500 to-blue-600 p-6 rounded-lg text-white">
                        <p className="text-sm opacity-90 mb-2">Net Present Value</p>
                        <p className="text-3xl font-bold">${currentProduct?.npv}M</p>
                        <p className="text-xs opacity-75 mt-2">As of {currentProduct?.lastUpdated}</p>
                      </div>
                      <div className="bg-gradient-to-br from-green-500 to-green-600 p-6 rounded-lg text-white">
                        <p className="text-sm opacity-90 mb-2">5-Year Revenue</p>
                        <p className="text-3xl font-bold">${(currentProduct?.npv * 1.8).toFixed(1)}M</p>
                        <p className="text-xs opacity-75 mt-2">Projected Total</p>
                      </div>
                      <div className="bg-gradient-to-br from-purple-500 to-purple-600 p-6 rounded-lg text-white">
                        <p className="text-sm opacity-90 mb-2">Peak Year Revenue</p>
                        <p className="text-3xl font-bold">${(currentProduct?.npv * 0.45).toFixed(1)}M</p>
                        <p className="text-xs opacity-75 mt-2">Year 4-5 Estimate</p>
                      </div>
                    </div>
                    
                    <div className="bg-gray-50 p-6 rounded-lg">
                      <h4 className="font-bold text-gray-800 mb-4">Revenue Waterfall (Year 1)</h4>
                      <div className="space-y-3">
                        <div className="flex items-center justify-between p-3 bg-white rounded">
                          <span className="text-sm text-gray-700">Gross Revenue (WAC)</span>
                          <span className="font-bold text-gray-900">$125.0M</span>
                        </div>
                        <div className="flex items-center justify-between p-3 bg-white rounded">
                          <span className="text-sm text-gray-700">- Rebates & Discounts</span>
                          <span className="font-bold text-red-600">-$42.5M</span>
                        </div>
                        <div className="flex items-center justify-between p-3 bg-white rounded">
                          <span className="text-sm text-gray-700">- Chargebacks</span>
                          <span className="font-bold text-red-600">-$8.2M</span>
                        </div>
                        <div className="flex items-center justify-between p-3 bg-white rounded">
                          <span className="text-sm text-gray-700">- Admin Fees</span>
                          <span className="font-bold text-red-600">-$6.8M</span>
                        </div>
                        <div className="flex items-center justify-between p-4 bg-blue-600 rounded text-white">
                          <span className="text-sm font-medium">Net Revenue</span>
                          <span className="font-bold text-xl">$67.5M</span>
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {activeTab === 'access' && (
                  <div className="space-y-6">
                    <div className="bg-yellow-50 border-l-4 border-yellow-500 p-4 rounded">
                      <div className="flex items-start">
                        <AlertCircle className="w-5 h-5 text-yellow-500 mr-3 mt-0.5" />
                        <div>
                          <p className="text-sm font-medium text-yellow-800">Market Access Strategy</p>
                          <p className="text-sm text-yellow-700 mt-1">
                            Based on {currentProduct?.archetype} archetype - focus on {currentProduct?.assumptions.distribution} channels
                          </p>
                        </div>
                      </div>
                    </div>

                    <div className="grid grid-cols-2 gap-6">
                      <div>
                        <h4 className="font-bold text-gray-800 mb-4">Target Payers</h4>
                        <div className="space-y-2">
                          {['UnitedHealthcare', 'CVS Caremark', 'Humana', 'Cigna', 'Aetna'].map((payer, idx) => (
                            <div key={payer} className="flex items-center justify-between p-3 bg-white rounded border">
                              <span className="text-sm text-gray-700">{payer}</span>
                              <span className={`text-xs px-2 py-1 rounded ${idx < 2 ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'}`}>
                                {idx < 2 ? 'High Priority' : 'Medium Priority'}
                              </span>
                            </div>
                          ))}
                        </div>
                      </div>

                      <div>
                        <h4 className="font-bold text-gray-800 mb-4">Key Milestones</h4>
                        <div className="space-y-3">
                          <div className="flex items-start space-x-3">
                            <div className="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center flex-shrink-0">
                              <Check className="w-5 h-5 text-green-600" />
                            </div>
                            <div className="flex-1">
                              <p className="text-sm font-medium text-gray-800">FDA Approval</p>
                              <p className="text-xs text-gray-500">Completed - 2025-Q4</p>
                            </div>
                          </div>
                          <div className="flex items-start space-x-3">
                            <div className="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center flex-shrink-0">
                              <div className="w-3 h-3 rounded-full bg-blue-600"></div>
                            </div>
                            <div className="flex-1">
                              <p className="text-sm font-medium text-gray-800">Payer Negotiations</p>
                              <p className="text-xs text-gray-500">In Progress - 2026-Q1</p>
                            </div>
                          </div>
                          <div className="flex items-start space-x-3">
                            <div className="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center flex-shrink-0">
                              <div className="w-3 h-3 rounded-full bg-gray-400"></div>
                            </div>
                            <div className="flex-1">
                              <p className="text-sm font-medium text-gray-800">Commercial Launch</p>
                              <p className="text-xs text-gray-500">Planned - 2026-Q2</p>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {activeTab === 'timeline' && (
                  <div className="space-y-4">
                    <div className="relative">
                      {['2025-Q4: FDA Approval', '2026-Q1: Payer Negotiations', '2026-Q2: Commercial Launch', '2026-Q3: Formulary Wins', '2026-Q4: Market Expansion'].map((milestone, idx) => (
                        <div key={idx} className="flex items-start mb-6 last:mb-0">
                          <div className="flex flex-col items-center mr-4">
                            <div className={`w-10 h-10 rounded-full flex items-center justify-center ${idx === 0 ? 'bg-green-500' : idx === 1 ? 'bg-blue-500' : 'bg-gray-300'}`}>
                              <span className="text-white font-bold text-sm">{idx + 1}</span>
                            </div>
                            {idx < 4 && <div className="w-1 h-12 bg-gray-300 mt-2"></div>}
                          </div>
                          <div className="flex-1 bg-white p-4 rounded-lg border border-gray-200">
                            <p className="font-medium text-gray-800">{milestone}</p>
                            <p className="text-xs text-gray-500 mt-1">
                              {idx === 0 ? 'Completed' : idx === 1 ? 'In Progress' : 'Upcoming'}
                            </p>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* Version History Panel */}
            {showVersionHistory && (
              <div className="bg-white rounded-lg shadow-md p-6">
                <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center">
                  <History className="w-5 h-5 mr-2 text-blue-600" />
                  Version History & Audit Trail
                </h3>
                <div className="space-y-3">
                  {versionHistory.map((version, idx) => (
                    <div
                      key={version.version}
                      className={`p-4 rounded-lg border-2 ${
                        idx === 0 ? 'border-blue-600 bg-blue-50' : 'border-gray-200 bg-white'
                      }`}
                    >
                      <div className="flex items-start justify-between mb-2">
                        <div>
                          <span className="font-bold text-gray-800">{version.version}</span>
                          <span className={`ml-2 text-xs px-2 py-1 rounded ${
                            version.status === 'Current' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'
                          }`}>
                            {version.status}
                          </span>
                        </div>
                        <div className="text-right">
                          <p className="text-sm font-medium text-gray-900">{version.user}</p>
                          <p className="text-xs text-gray-500">{version.date}</p>
                        </div>
                      </div>
                      <div className="space-y-1 mb-2">
                        {version.changes.map((change, changeIdx) => (
                          <p key={changeIdx} className="text-sm text-gray-700 flex items-start">
                            <span className="text-blue-600 mr-2">•</span>
                            {change}
                          </p>
                        ))}
                      </div>
                      <div className="flex items-center justify-between pt-2 border-t border-gray-200">
                        <span className="text-xs text-gray-600">NPV Impact</span>
                        <span className={`text-sm font-bold ${version.npvImpact > 0 ? 'text-green-600' : version.npvImpact < 0 ? 'text-red-600' : 'text-gray-600'}`}>
                          {version.npvImpact > 0 ? '+' : ''}{version.npvImpact}M
                        </span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Scenario Comparison */}
            {showScenarioComparison && (
              <div className="bg-white rounded-lg shadow-md p-6">
                <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center">
                  <GitBranch className="w-5 h-5 mr-2 text-purple-600" />
                  Scenario Comparison
                </h3>
                <div className="overflow-x-auto">
                  <table className="w-full">
                    <thead className="bg-gray-50">
                      <tr>
                        <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Metric</th>
                        <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Base Case</th>
                        <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Optimistic</th>
                        <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Conservative</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-200">
                      <tr>
                        <td className="px-4 py-3 text-sm font-medium text-gray-900">NPV</td>
                        <td className="px-4 py-3 text-sm text-gray-900">${currentProduct?.npv}M</td>
                        <td className="px-4 py-3 text-sm text-green-600 font-medium">${(currentProduct?.npv * 1.25).toFixed(1)}M</td>
                        <td className="px-4 py-3 text-sm text-red-600 font-medium">${(currentProduct?.npv * 0.75).toFixed(1)}M</td>
                      </tr>
                      <tr>
                        <td className="px-4 py-3 text-sm font-medium text-gray-900">Peak Share</td>
                        <td className="px-4 py-3 text-sm text-gray-900">{currentProduct?.assumptions.peakShare}%</td>
                        <td className="px-4 py-3 text-sm text-green-600 font-medium">{currentProduct?.assumptions.peakShare + 8}%</td>
                        <td className="px-4 py-3 text-sm text-red-600 font-medium">{currentProduct?.assumptions.peakShare - 8}%</td>
                      </tr>
                      <tr>
                        <td className="px-4 py-3 text-sm font-medium text-gray-900">GTN %</td>
                        <td className="px-4 py-3 text-sm text-gray-900">{currentProduct?.assumptions.pricing.gtn}%</td>
                        <td className="px-4 py-3 text-sm text-green-600 font-medium">{currentProduct?.assumptions.pricing.gtn - 5}%</td>
                        <td className="px-4 py-3 text-sm text-red-600 font-medium">{currentProduct?.assumptions.pricing.gtn + 5}%</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Footer */}
      <div className="mt-6 bg-white rounded-lg shadow-md p-4">
        <div className="flex items-center justify-between text-sm text-gray-600">
          <div className="flex items-center space-x-4">
            <span className="flex items-center">
              <Users className="w-4 h-4 mr-1" />
              Last updated by {currentProduct?.updatedBy}
            </span>
            <span className="flex items-center">
              <Calendar className="w-4 h-4 mr-1" />
              {currentProduct?.lastUpdated}
            </span>
          </div>
          <div className="flex items-center space-x-2">
            <span className="text-xs text-gray-500">Single Source of Truth | Version Control Enabled</span>
            <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SandozPipelinePlatform;