// TCP Systems Data - Product Catalog and Sales Configuration

export interface ProductSystem {
  id: string;
  name: string;
  category: string;
  description: string;
  basePricePerSqFt: number;
  features: string[];
  recommendedFor: string[];
}

export interface TextureOption {
  id: string;
  code: string;
  name: string;
  description: string;
  slipResistance: 'Low' | 'Medium' | 'High';
  maintenanceLevel: 'Easy' | 'Moderate' | 'Detailed';
  bestFor: string[];
}

export interface ColorOption {
  id: string;
  name: string;
  hex: string;
  category: 'Earth Tones' | 'Grays' | 'Blues' | 'Reds' | 'Custom';
  popularity: 'High' | 'Medium' | 'Low';
}

export interface DesignOption {
  id: string;
  type: 'Pattern' | 'Border' | 'Logo';
  name: string;
  description: string;
  complexity: 'Simple' | 'Moderate' | 'Complex';
  additionalCostPerSqFt: number;
}

export interface TopCoatOption {
  id: string;
  name: string;
  description: string;
  durability: 'Standard' | 'Enhanced' | 'Premium';
  uvResistance: 'None' | 'Standard' | 'High';
  chemicalResistance: 'Basic' | 'Enhanced' | 'Maximum';
  additionalCostPerSqFt: number;
}

export interface LocationFactor {
  id: string;
  name: string;
  description: string;
  considerations: string[];
}

// Product Systems by Category
export const productSystems: ProductSystem[] = [
  // CEMENTS OVERLAYS
  {
    id: 'rustic-concrete-wood',
    name: 'Rustic Concrete Wood',
    category: 'Cements Overlays',
    description: 'Authentic wood-grain appearance with concrete durability',
    basePricePerSqFt: 8.50,
    features: ['Wood-grain texture', 'UV resistant', 'Slip resistant', 'Low maintenance'],
    recommendedFor: ['Patios', 'Pool decks', 'Walkways', 'Indoor flooring']
  },
  {
    id: 'tuscan-slate',
    name: 'Tuscan Slate',
    category: 'Cements Overlays',
    description: 'Elegant slate appearance with old-world charm',
    basePricePerSqFt: 9.00,
    features: ['Natural slate look', 'Multiple color options', 'Durable finish', 'Weather resistant'],
    recommendedFor: ['Entryways', 'Living rooms', 'Commercial spaces', 'Outdoor patios']
  },
  {
    id: 'grand-flagstone',
    name: 'Grand Flagstone',
    category: 'Cements Overlays',
    description: 'Large format flagstone pattern for grand spaces',
    basePricePerSqFt: 9.50,
    features: ['Large stone pattern', 'Natural variation', 'Seamless finish', 'Heavy duty'],
    recommendedFor: ['Large patios', 'Driveways', 'Commercial floors', 'Pool surrounds']
  },
  {
    id: 'venetian-tile',
    name: 'Venetian Tile',
    category: 'Cements Overlays',
    description: 'Classic tile appearance without grout lines',
    basePricePerSqFt: 8.00,
    features: ['No grout maintenance', 'Uniform appearance', 'Water resistant', 'Easy to clean'],
    recommendedFor: ['Kitchens', 'Bathrooms', 'Laundry rooms', 'Basements']
  },
  
  // EPOXY & URETHANES
  {
    id: 'metallic-marble-stain',
    name: 'Metallic Marble Stain',
    category: 'Epoxy & Urethanes',
    description: 'Stunning metallic finish with marble-like depth',
    basePricePerSqFt: 7.50,
    features: ['3D metallic effect', 'Unique patterns', 'Glossy finish', 'Chemical resistant'],
    recommendedFor: ['Showrooms', 'Garages', 'Man caves', 'Retail spaces']
  },
  {
    id: 'italian-marble-epoxy',
    name: 'Italian Marble Epoxy',
    category: 'Epoxy & Urethanes',
    description: 'Luxurious marble appearance with epoxy durability',
    basePricePerSqFt: 10.00,
    features: ['Marble veining', 'High gloss', 'Scratch resistant', 'Long lasting'],
    recommendedFor: ['Lobbies', 'High-end homes', 'Hotels', 'Office buildings']
  },
  {
    id: 'resinous-123-floor',
    name: 'Resinous 123 Floor',
    category: 'Epoxy & Urethanes',
    description: 'Three-coat system for maximum durability',
    basePricePerSqFt: 6.50,
    features: ['Three-layer system', 'Industrial strength', 'Chemical resistant', 'Seamless'],
    recommendedFor: ['Warehouses', 'Factories', 'Garages', 'Workshops']
  },
  {
    id: 'protector-flake',
    name: 'Protector Flake',
    category: 'Epoxy & Urethanes',
    description: 'Decorative flake system with excellent coverage',
    basePricePerSqFt: 5.50,
    features: ['Color flakes', 'Hides imperfections', 'Slip resistant', 'Easy maintenance'],
    recommendedFor: ['Garages', 'Basements', 'Workshops', 'Laundry rooms']
  },
  {
    id: 'protector-quartz',
    name: 'Protector Quartz',
    category: 'Epoxy & Urethanes',
    description: 'Quartz aggregate for durability and aesthetics',
    basePricePerSqFt: 7.00,
    features: ['Quartz aggregate', 'Non-slip surface', 'Highly durable', 'Decorative'],
    recommendedFor: ['Pool decks', 'Locker rooms', 'Commercial kitchens', 'Outdoor spaces']
  },
  
  // GRANIFLEX
  {
    id: 'graniflex-flake',
    name: 'Graniflex Flake',
    category: 'Graniflex',
    description: 'Flexible coating with decorative flakes',
    basePricePerSqFt: 8.00,
    features: ['Flexible formula', 'Crack bridging', 'Decorative flakes', 'UV stable'],
    recommendedFor: ['Pool decks', 'Patios', 'Driveways', 'Balconies']
  },
  {
    id: 'graniflex-quartz',
    name: 'Graniflex Quartz',
    category: 'Graniflex',
    description: 'Flexible coating with quartz aggregate',
    basePricePerSqFt: 8.50,
    features: ['Flexible formula', 'Quartz texture', 'Non-slip', 'Weather resistant'],
    recommendedFor: ['Commercial pools', 'Water parks', 'Public spaces', 'Outdoor walkways']
  },
  {
    id: 'marble-flex',
    name: 'Marble Flex',
    category: 'Graniflex',
    description: 'Flexible marble-looking coating system',
    basePricePerSqFt: 11.00,
    features: ['Marble appearance', 'Flexible substrate', 'Luxury finish', 'Crack resistant'],
    recommendedFor: ['Luxury homes', 'Hotels', 'Spas', 'High-traffic areas']
  },
  
  // POLYHARD
  {
    id: 'polyhard-colored',
    name: 'Polyhard Colored',
    category: 'Polyhard',
    description: 'Hard-wearing colored polyaspartic coating',
    basePricePerSqFt: 6.00,
    features: ['Fast cure', 'UV stable', 'Color options', 'Durable'],
    recommendedFor: ['Garages', 'Commercial floors', 'Industrial spaces', 'Showrooms']
  },
  {
    id: 'polyhard-quartz',
    name: 'Polyhard Quartz',
    category: 'Polyhard',
    description: 'Polyaspartic with quartz for enhanced durability',
    basePricePerSqFt: 7.50,
    features: ['Quartz aggregate', 'Fast installation', 'Non-slip', 'Chemical resistant'],
    recommendedFor: ['Industrial floors', 'Commercial kitchens', 'Workshops', 'Warehouses']
  },
  
  // SCIENTIFIC CONCRETE POLISHING
  {
    id: 'scp-wet',
    name: 'SCP Wet',
    category: 'Scientific Concrete Polishing',
    description: 'Wet polishing system for superior finish',
    basePricePerSqFt: 5.00,
    features: ['Wet process', 'Dust-free', 'High shine', 'Environmentally friendly'],
    recommendedFor: ['Indoor floors', 'Commercial spaces', 'Homes', 'Retail stores']
  },
  {
    id: 'scp-dry',
    name: 'SCP Dry',
    category: 'Scientific Concrete Polishing',
    description: 'Dry polishing system for faster completion',
    basePricePerSqFt: 4.50,
    features: ['Fast process', 'No water needed', 'Glossy finish', 'Cost effective'],
    recommendedFor: ['Warehouses', 'Industrial spaces', 'Large areas', 'Budget projects']
  },
  
  // CP SEALER
  {
    id: 'cp-sealer',
    name: 'CP Sealer',
    category: 'CP Sealer',
    description: 'Professional grade concrete sealer',
    basePricePerSqFt: 2.00,
    features: ['Deep penetration', 'Water repellent', 'Stain resistant', 'Long lasting'],
    recommendedFor: ['Driveways', 'Patios', 'Walkways', 'Any concrete surface']
  },
  
  // REPAIRS & JOINTS FILL
  {
    id: 'repairs-joints-fill',
    name: 'Repairs & Joints Fill',
    category: 'Repairs & Joints Fill',
    description: 'Professional repair and joint filling solutions',
    basePricePerSqFt: 3.00,
    features: ['Crack repair', 'Joint filling', 'Leveling', 'Surface restoration'],
    recommendedFor: ['Damaged concrete', 'Expansion joints', 'Crack remediation', 'Surface prep']
  }
];

// Surface Texture Options
export const textureOptions: TextureOption[] = [
  {
    id: 't1',
    code: 'T-1',
    name: 'Mountain & Valleys',
    description: 'Deep texture with pronounced highs and lows for maximum slip resistance',
    slipResistance: 'High',
    maintenanceLevel: 'Detailed',
    bestFor: ['Pool decks', 'Outdoor areas', 'Sloped surfaces', 'Wet environments']
  },
  {
    id: 't2',
    code: 'T-2',
    name: 'Mountains',
    description: 'Moderate texture with consistent pattern for balanced performance',
    slipResistance: 'Medium',
    maintenanceLevel: 'Moderate',
    bestFor: ['Patios', 'Walkways', 'Driveways', 'General outdoor use']
  },
  {
    id: 't3',
    code: 'T-3',
    name: 'Smooth (Few Islands)',
    description: 'Light texture with smooth areas for easy cleaning and modern look',
    slipResistance: 'Low',
    maintenanceLevel: 'Easy',
    bestFor: ['Indoor floors', 'Showrooms', 'Living spaces', 'Commercial interiors']
  }
];

// Color Options
export const colorOptions: ColorOption[] = [
  // Earth Tones
  { id: 'desert-sand', name: 'Desert Sand', hex: '#C2B280', category: 'Earth Tones', popularity: 'High' },
  { id: 'tuscan-gold', name: 'Tuscan Gold', hex: '#D4A84B', category: 'Earth Tones', popularity: 'High' },
  { id: 'terra-cotta', name: 'Terra Cotta', hex: '#E2725B', category: 'Earth Tones', popularity: 'Medium' },
  { id: 'mocha', name: 'Mocha', hex: '#7B5B4A', category: 'Earth Tones', popularity: 'Medium' },
  { id: 'sienna', name: 'Sienna', hex: '#A0522D', category: 'Earth Tones', popularity: 'High' },
  { id: 'saddle-brown', name: 'Saddle Brown', hex: '#8B4513', category: 'Earth Tones', popularity: 'Medium' },
  
  // Grays
  { id: 'charcoal', name: 'Charcoal', hex: '#36454F', category: 'Grays', popularity: 'High' },
  { id: 'slate-gray', name: 'Slate Gray', hex: '#708090', category: 'Grays', popularity: 'High' },
  { id: 'platinum', name: 'Platinum', hex: '#E5E4E2', category: 'Grays', popularity: 'Medium' },
  { id: 'gunmetal', name: 'Gunmetal', hex: '#2C3539', category: 'Grays', popularity: 'High' },
  { id: 'pewter', name: 'Pewter', hex: '#899499', category: 'Grays', popularity: 'Low' },
  { id: 'cloud-gray', name: 'Cloud Gray', hex: '#C4C4C4', category: 'Grays', popularity: 'Medium' },
  
  // Blues
  { id: 'ocean-blue', name: 'Ocean Blue', hex: '#4F42B5', category: 'Blues', popularity: 'Medium' },
  { id: 'midnight', name: 'Midnight', hex: '#191970', category: 'Blues', popularity: 'Low' },
  { id: 'denim', name: 'Denim', hex: '#1560BD', category: 'Blues', popularity: 'Medium' },
  { id: 'teal', name: 'Teal', hex: '#008080', category: 'Blues', popularity: 'Medium' },
  
  // Reds
  { id: 'brick-red', name: 'Brick Red', hex: '#CB4154', category: 'Reds', popularity: 'Low' },
  { id: 'rust', name: 'Rust', hex: '#B7410E', category: 'Reds', popularity: 'Medium' },
  { id: 'mahogany', name: 'Mahogany', hex: '#C04000', category: 'Reds', popularity: 'Low' },
  
  // Custom
  { id: 'custom-color', name: 'Custom Color Match', hex: '#888888', category: 'Custom', popularity: 'Low' }
];

// Design Options
export const designOptions: DesignOption[] = [
  // Patterns
  { id: 'ashlar-pattern', type: 'Pattern', name: 'Ashlar Pattern', description: 'Random rectangular stone pattern', complexity: 'Simple', additionalCostPerSqFt: 0.50 },
  { id: 'herringbone-pattern', type: 'Pattern', name: 'Herringbone', description: 'Classic V-shaped pattern', complexity: 'Moderate', additionalCostPerSqFt: 1.00 },
  { id: 'cobblestone-pattern', type: 'Pattern', name: 'Cobblestone', description: 'European-style rounded stone look', complexity: 'Moderate', additionalCostPerSqFt: 0.75 },
  { id: 'flagstone-pattern', type: 'Pattern', name: 'Flagstone', description: 'Natural irregular stone pattern', complexity: 'Simple', additionalCostPerSqFt: 0.50 },
  { id: 'brick-pattern', type: 'Pattern', name: 'Brick Pattern', description: 'Traditional running bond brick look', complexity: 'Simple', additionalCostPerSqFt: 0.25 },
  { id: 'random-stone', type: 'Pattern', name: 'Random Stone', description: 'Natural random stone appearance', complexity: 'Moderate', additionalCostPerSqFt: 0.75 },
  
  // Borders
  { id: 'soldier-border', type: 'Border', name: 'Soldier Border', description: 'Straight lined border pattern', complexity: 'Simple', additionalCostPerSqFt: 2.00 },
  { id: 'rope-border', type: 'Border', name: 'Rope Border', description: 'Twisted rope design border', complexity: 'Moderate', additionalCostPerSqFt: 3.50 },
  { id: 'scroll-border', type: 'Border', name: 'Scroll Border', description: 'Elegant scrollwork design', complexity: 'Complex', additionalCostPerSqFt: 5.00 },
  { id: 'geometric-border', type: 'Border', name: 'Geometric Border', description: 'Modern geometric shapes', complexity: 'Moderate', additionalCostPerSqFt: 3.00 },
  { id: 'diamond-border', type: 'Border', name: 'Diamond Border', description: 'Diamond-shaped accent border', complexity: 'Simple', additionalCostPerSqFt: 2.50 },
  
  // Logos
  { id: 'simple-logo', type: 'Logo', name: 'Simple Logo', description: 'Basic single-color logo', complexity: 'Simple', additionalCostPerSqFt: 0 },
  { id: 'detailed-logo', type: 'Logo', name: 'Detailed Logo', description: 'Multi-color detailed logo', complexity: 'Moderate', additionalCostPerSqFt: 0 },
  { id: 'custom-artwork', type: 'Logo', name: 'Custom Artwork', description: 'Custom artistic design', complexity: 'Complex', additionalCostPerSqFt: 0 }
];

// Top Coat Options
export const topCoatOptions: TopCoatOption[] = [
  {
    id: 'standard-clear',
    name: 'Standard Clear',
    description: 'Basic clear protective top coat',
    durability: 'Standard',
    uvResistance: 'Standard',
    chemicalResistance: 'Basic',
    additionalCostPerSqFt: 0.50
  },
  {
    id: 'enhanced-uv',
    name: 'Enhanced UV Protection',
    description: 'UV-resistant top coat for outdoor applications',
    durability: 'Enhanced',
    uvResistance: 'High',
    chemicalResistance: 'Enhanced',
    additionalCostPerSqFt: 1.00
  },
  {
    id: 'high-gloss',
    name: 'High Gloss Finish',
    description: 'Ultra-glossy top coat for maximum shine',
    durability: 'Enhanced',
    uvResistance: 'Standard',
    chemicalResistance: 'Enhanced',
    additionalCostPerSqFt: 0.75
  },
  {
    id: 'matte-finish',
    name: 'Matte Finish',
    description: 'Low-sheen matte top coat for modern look',
    durability: 'Standard',
    uvResistance: 'Standard',
    chemicalResistance: 'Basic',
    additionalCostPerSqFt: 0.50
  },
  {
    id: 'industrial-grade',
    name: 'Industrial Grade',
    description: 'Maximum protection for heavy-duty applications',
    durability: 'Premium',
    uvResistance: 'High',
    chemicalResistance: 'Maximum',
    additionalCostPerSqFt: 1.50
  },
  {
    id: 'anti-graffiti',
    name: 'Anti-Graffiti Coating',
    description: 'Protective coating resistant to graffiti and stains',
    durability: 'Premium',
    uvResistance: 'High',
    chemicalResistance: 'Maximum',
    additionalCostPerSqFt: 2.00
  }
];

// Location Factors
export const locationFactors: LocationFactor[] = [
  {
    id: 'indoor-residential',
    name: 'Indoor Residential',
    description: 'Interior spaces in homes',
    considerations: ['Lower slip resistance acceptable', 'UV protection less critical', 'Aesthetics priority', 'Low odor products recommended']
  },
  {
    id: 'indoor-commercial',
    name: 'Indoor Commercial',
    description: 'Interior commercial and retail spaces',
    considerations: ['High traffic durability', 'Low maintenance', 'Professional appearance', 'Quick installation preferred']
  },
  {
    id: 'outdoor-residential',
    name: 'Outdoor Residential',
    description: 'Exterior residential areas',
    considerations: ['UV resistance critical', 'Weather durability', 'Slip resistance important', 'Temperature fluctuation tolerance']
  },
  {
    id: 'outdoor-commercial',
    name: 'Outdoor Commercial',
    description: 'Exterior commercial spaces',
    considerations: ['Heavy traffic resistance', 'Maximum UV protection', 'High slip resistance', 'Low maintenance priority']
  },
  {
    id: 'pool-deck',
    name: 'Pool Deck',
    description: 'Swimming pool surrounds',
    considerations: ['Maximum slip resistance', 'Chlorine resistance', 'Cool surface preferred', 'Water drainage considerations']
  },
  {
    id: 'garage',
    name: 'Garage / Workshop',
    description: 'Vehicle and work spaces',
    considerations: ['Oil and chemical resistance', 'Impact resistance', 'Easy to clean', 'Hot tire pickup resistance']
  }
];

// Installation Steps
export const installationSteps = [
  { step: 1, name: 'Surface Preparation', options: ['Grind', 'Shot Blast', 'Acid Wash', 'Other'] },
  { step: 2, name: 'Repair & Joints', options: ['Fill Cracks', 'Joint Treatment', 'Leveling'] },
  { step: 3, name: 'Prime Coat Application', options: ['Standard Prime', 'Moisture Barrier', 'Epoxy Prime'] },
  { step: 4, name: 'Design Layout', options: ['Mark Pattern', 'Set Borders', 'Position Logo'] },
  { step: 5, name: 'Intermediate Coat Application', options: ['Base Coat', 'Texture Coat', 'Color Coat'] },
  { step: 6, name: 'Seal Coat Application', options: ['Standard Seal', 'Enhanced Seal'] },
  { step: 7, name: 'Top Coat Application', options: ['Clear Top Coat', 'Gloss Finish', 'Matte Finish'] }
];

// Get unique categories
export const getProductCategories = (): string[] => {
  return [...new Set(productSystems.map(p => p.category))];
};

// Get products by category
export const getProductsByCategory = (category: string): ProductSystem[] => {
  return productSystems.filter(p => p.category === category);
};

// Get design options by type
export const getDesignOptionsByType = (type: 'Pattern' | 'Border' | 'Logo'): DesignOption[] => {
  return designOptions.filter(d => d.type === type);
};

// Get colors by category
export const getColorsByCategory = (category: ColorOption['category']): ColorOption[] => {
  return colorOptions.filter(c => c.category === category);
};
