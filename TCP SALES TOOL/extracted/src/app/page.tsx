"use client";

import { useState, useMemo } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Checkbox } from "@/components/ui/checkbox";
import { Progress } from "@/components/ui/progress";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import { 
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";
import { 
  Palette, 
  Layers, 
  Droplets, 
  MapPin, 
  CheckCircle2, 
  Circle, 
  Building2,
  Paintbrush,
  Sparkles,
  Shield,
  Calculator,
  FileText,
  Download,
  Share2,
  Info,
  Star,
  ArrowRight,
  ArrowLeft,
  Plus,
  Minus,
  RefreshCw,
  Copy,
  Check
} from "lucide-react";
import { useToast } from "@/hooks/use-toast";
import {
  productSystems,
  textureOptions,
  colorOptions,
  designOptions,
  topCoatOptions,
  locationFactors,
  installationSteps,
  getProductCategories,
  type ProductSystem,
  type TextureOption,
  type ColorOption,
  type DesignOption,
  type TopCoatOption,
  type LocationFactor
} from "@/lib/tcp-data";

// Sales Configuration State Type
interface SalesConfig {
  // Project Info
  customerName: string;
  projectAddress: string;
  projectNotes: string;
  squareFootage: number;
  
  // Location & Performance
  locationType: string;
  performancePriority: string;
  
  // System Selection
  selectedProduct: ProductSystem | null;
  
  // Design Options
  selectedPattern: DesignOption | null;
  selectedBorder: DesignOption | null;
  selectedLogo: DesignOption | null;
  
  // Color Selection
  primaryColor: ColorOption | null;
  secondaryColor: ColorOption | null;
  
  // Texture
  selectedTexture: TextureOption | null;
  
  // Top Coat
  selectedTopCoat: TopCoatOption | null;
}

const initialConfig: SalesConfig = {
  customerName: "",
  projectAddress: "",
  projectNotes: "",
  squareFootage: 500,
  locationType: "",
  performancePriority: "",
  selectedProduct: null,
  selectedPattern: null,
  selectedBorder: null,
  selectedLogo: null,
  primaryColor: null,
  secondaryColor: null,
  selectedTexture: null,
  selectedTopCoat: null
};

export default function TCPSalesTool() {
  const [config, setConfig] = useState<SalesConfig>(initialConfig);
  const [currentStep, setCurrentStep] = useState(0);
  const [copied, setCopied] = useState(false);
  const { toast } = useToast();

  const categories = getProductCategories();
  const patterns = designOptions.filter(d => d.type === 'Pattern');
  const borders = designOptions.filter(d => d.type === 'Border');
  const logos = designOptions.filter(d => d.type === 'Logo');

  // Calculate total estimate
  const estimate = useMemo(() => {
    if (!config.selectedProduct) return null;
    
    let baseCost = config.selectedProduct.basePricePerSqFt * config.squareFootage;
    
    // Add design costs
    if (config.selectedPattern) {
      baseCost += config.selectedPattern.additionalCostPerSqFt * config.squareFootage;
    }
    if (config.selectedBorder) {
      // Border typically costs per linear foot, estimate 10% of perimeter
      const perimeterEstimate = Math.sqrt(config.squareFootage) * 4;
      baseCost += config.selectedBorder.additionalCostPerSqFt * perimeterEstimate;
    }
    
    // Add texture cost (if different from base)
    
    // Add top coat cost
    if (config.selectedTopCoat) {
      baseCost += config.selectedTopCoat.additionalCostPerSqFt * config.squareFootage;
    }
    
    return {
      baseCost,
      perSqFt: baseCost / config.squareFootage,
      breakdown: {
        product: config.selectedProduct.basePricePerSqFt,
        pattern: config.selectedPattern?.additionalCostPerSqFt || 0,
        border: config.selectedBorder?.additionalCostPerSqFt || 0,
        topCoat: config.selectedTopCoat?.additionalCostPerSqFt || 0
      }
    };
  }, [config]);

  // Step configuration
  const steps = [
    { id: 'location', title: 'Location & Performance', icon: MapPin },
    { id: 'system', title: 'System Selection', icon: Layers },
    { id: 'design', title: 'Design Options', icon: Paintbrush },
    { id: 'colors', title: 'Colors', icon: Palette },
    { id: 'texture', title: 'Surface Texture', icon: Droplets },
    { id: 'topcoat', title: 'Top Coat', icon: Shield },
    { id: 'summary', title: 'Quote Summary', icon: FileText }
  ];

  const completedSteps = useMemo(() => {
    const completed: string[] = [];
    if (config.locationType && config.performancePriority) completed.push('location');
    if (config.selectedProduct) completed.push('system');
    if (config.selectedPattern || config.selectedBorder || config.selectedLogo) completed.push('design');
    if (config.primaryColor) completed.push('colors');
    if (config.selectedTexture) completed.push('texture');
    if (config.selectedTopCoat) completed.push('topcoat');
    return completed;
  }, [config]);

  const progress = (completedSteps.length / steps.length) * 100;

  // Update handlers
  const updateConfig = <K extends keyof SalesConfig>(key: K, value: SalesConfig[K]) => {
    setConfig(prev => ({ ...prev, [key]: value }));
  };

  const handleNext = () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1);
    }
  };

  const handlePrev = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  const handleReset = () => {
    setConfig(initialConfig);
    setCurrentStep(0);
    toast({
      title: "Configuration Reset",
      description: "All selections have been cleared."
    });
  };

  const generateQuoteText = () => {
    const lines = [
      "═══════════════════════════════════════════════",
      "THE CONCRETE PROTECTOR - SALES QUOTE",
      "═══════════════════════════════════════════════",
      "",
      `Customer: ${config.customerName || 'Not specified'}`,
      `Project Address: ${config.projectAddress || 'Not specified'}`,
      `Square Footage: ${config.squareFootage.toLocaleString()} sq ft`,
      "",
      "───────────────────────────────────────────────",
      "SYSTEM SELECTION",
      "───────────────────────────────────────────────",
      config.selectedProduct ? [
        `Product: ${config.selectedProduct.name}`,
        `Category: ${config.selectedProduct.category}`,
        `Base Price: $${config.selectedProduct.basePricePerSqFt.toFixed(2)}/sq ft`
      ].join('\n') : 'No product selected',
      "",
      "───────────────────────────────────────────────",
      "DESIGN OPTIONS",
      "───────────────────────────────────────────────",
      config.selectedPattern ? `Pattern: ${config.selectedPattern.name} (+$${config.selectedPattern.additionalCostPerSqFt.toFixed(2)}/sq ft)` : 'Pattern: None',
      config.selectedBorder ? `Border: ${config.selectedBorder.name} (+$${config.selectedBorder.additionalCostPerSqFt.toFixed(2)}/ln ft)` : 'Border: None',
      config.selectedLogo ? `Logo: ${config.selectedLogo.name}` : 'Logo: None',
      "",
      "───────────────────────────────────────────────",
      "COLOR SELECTION",
      "───────────────────────────────────────────────",
      config.primaryColor ? `Primary Color: ${config.primaryColor.name}` : 'Primary Color: Not selected',
      config.secondaryColor ? `Secondary Color: ${config.secondaryColor.name}` : 'Secondary Color: Not selected',
      "",
      "───────────────────────────────────────────────",
      "SURFACE TEXTURE",
      "───────────────────────────────────────────────",
      config.selectedTexture ? [
        `Texture: ${config.selectedTexture.code} - ${config.selectedTexture.name}`,
        `Slip Resistance: ${config.selectedTexture.slipResistance}`,
        `Maintenance: ${config.selectedTexture.maintenanceLevel}`
      ].join('\n') : 'No texture selected',
      "",
      "───────────────────────────────────────────────",
      "TOP COAT",
      "───────────────────────────────────────────────",
      config.selectedTopCoat ? [
        `Top Coat: ${config.selectedTopCoat.name}`,
        `Durability: ${config.selectedTopCoat.durability}`,
        `UV Resistance: ${config.selectedTopCoat.uvResistance}`,
        `Chemical Resistance: ${config.selectedTopCoat.chemicalResistance}`,
        `Additional Cost: $${config.selectedTopCoat.additionalCostPerSqFt.toFixed(2)}/sq ft`
      ].join('\n') : 'No top coat selected',
      "",
      "═══════════════════════════════════════════════",
      "ESTIMATED COST",
      "═══════════════════════════════════════════════",
      estimate ? [
        `Per Square Foot: $${estimate.perSqFt.toFixed(2)}`,
        `Total Estimate: $${estimate.baseCost.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`
      ].join('\n') : 'Unable to calculate',
      "",
      `Notes: ${config.projectNotes || 'None'}`,
      "",
      "═══════════════════════════════════════════════"
    ];
    return lines.join('\n');
  };

  const copyToClipboard = async () => {
    const quoteText = generateQuoteText();
    await navigator.clipboard.writeText(quoteText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
    toast({
      title: "Copied to Clipboard",
      description: "Quote details have been copied."
    });
  };

  // Render step content
  const renderStepContent = () => {
    switch (steps[currentStep].id) {
      case 'location':
        return (
          <div className="space-y-6">
            {/* Project Info */}
            <Card>
              <CardHeader>
                <CardTitle className="text-lg flex items-center gap-2">
                  <Building2 className="h-5 w-5" />
                  Project Information
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid gap-4 md:grid-cols-2">
                  <div className="space-y-2">
                    <Label htmlFor="customerName">Customer Name</Label>
                    <Input
                      id="customerName"
                      placeholder="Enter customer name"
                      value={config.customerName}
                      onChange={(e) => updateConfig('customerName', e.target.value)}
                    />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="squareFootage">Square Footage</Label>
                    <Input
                      id="squareFootage"
                      type="number"
                      min={100}
                      value={config.squareFootage}
                      onChange={(e) => updateConfig('squareFootage', parseInt(e.target.value) || 0)}
                    />
                  </div>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="projectAddress">Project Address</Label>
                  <Input
                    id="projectAddress"
                    placeholder="Enter project address"
                    value={config.projectAddress}
                    onChange={(e) => updateConfig('projectAddress', e.target.value)}
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="projectNotes">Project Notes</Label>
                  <Textarea
                    id="projectNotes"
                    placeholder="Enter any project notes or special requirements"
                    value={config.projectNotes}
                    onChange={(e) => updateConfig('projectNotes', e.target.value)}
                  />
                </div>
              </CardContent>
            </Card>

            {/* Location Type */}
            <Card>
              <CardHeader>
                <CardTitle className="text-lg flex items-center gap-2">
                  <MapPin className="h-5 w-5" />
                  Location Type
                </CardTitle>
                <CardDescription>Select the project location type</CardDescription>
              </CardHeader>
              <CardContent>
                <RadioGroup
                  value={config.locationType}
                  onValueChange={(value) => updateConfig('locationType', value)}
                  className="grid gap-3 md:grid-cols-2"
                >
                  {locationFactors.map((location) => (
                    <div key={location.id} className="flex items-start space-x-3 p-3 rounded-lg border hover:bg-muted/50 transition-colors">
                      <RadioGroupItem value={location.id} id={location.id} className="mt-1" />
                      <div className="space-y-1">
                        <Label htmlFor={location.id} className="font-medium cursor-pointer">
                          {location.name}
                        </Label>
                        <p className="text-sm text-muted-foreground">{location.description}</p>
                        <div className="flex flex-wrap gap-1 mt-2">
                          {location.considerations.slice(0, 2).map((c, i) => (
                            <Badge key={i} variant="secondary" className="text-xs">{c}</Badge>
                          ))}
                        </div>
                      </div>
                    </div>
                  ))}
                </RadioGroup>
              </CardContent>
            </Card>

            {/* Performance Priority */}
            <Card>
              <CardHeader>
                <CardTitle className="text-lg">Performance Priority</CardTitle>
                <CardDescription>What is most important for this project?</CardDescription>
              </CardHeader>
              <CardContent>
                <RadioGroup
                  value={config.performancePriority}
                  onValueChange={(value) => updateConfig('performancePriority', value)}
                  className="grid gap-3 md:grid-cols-3"
                >
                  {[
                    { id: 'durability', label: 'Durability', desc: 'Maximum lifespan and wear resistance', icon: Shield },
                    { id: 'aesthetics', label: 'Aesthetics', desc: 'Visual appeal and design options', icon: Sparkles },
                    { id: 'budget', label: 'Budget', desc: 'Cost-effective solution', icon: Calculator }
                  ].map((option) => (
                    <div key={option.id} className="flex items-center space-x-3 p-4 rounded-lg border hover:bg-muted/50 transition-colors cursor-pointer">
                      <RadioGroupItem value={option.id} id={option.id} />
                      <option.icon className="h-5 w-5 text-muted-foreground" />
                      <div>
                        <Label htmlFor={option.id} className="font-medium cursor-pointer">{option.label}</Label>
                        <p className="text-sm text-muted-foreground">{option.desc}</p>
                      </div>
                    </div>
                  ))}
                </RadioGroup>
              </CardContent>
            </Card>
          </div>
        );

      case 'system':
        return (
          <div className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="text-lg flex items-center gap-2">
                  <Layers className="h-5 w-5" />
                  Select Product System
                </CardTitle>
                <CardDescription>Choose the concrete coating system for this project</CardDescription>
              </CardHeader>
              <CardContent>
                <Accordion type="multiple" className="w-full">
                  {categories.map((category) => (
                    <AccordionItem key={category} value={category}>
                      <AccordionTrigger className="hover:no-underline">
                        <div className="flex items-center gap-2">
                          <span className="font-semibold">{category}</span>
                          <Badge variant="outline">
                            {productSystems.filter(p => p.category === category).length} products
                          </Badge>
                        </div>
                      </AccordionTrigger>
                      <AccordionContent>
                        <div className="grid gap-4 md:grid-cols-2 pt-2">
                          {productSystems.filter(p => p.category === category).map((product) => (
                            <div
                              key={product.id}
                              className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                                config.selectedProduct?.id === product.id
                                  ? 'border-primary bg-primary/5'
                                  : 'border-transparent bg-muted/50 hover:border-primary/50'
                              }`}
                              onClick={() => updateConfig('selectedProduct', product)}
                            >
                              <div className="flex justify-between items-start mb-2">
                                <h4 className="font-semibold">{product.name}</h4>
                                <Badge variant="secondary">${product.basePricePerSqFt.toFixed(2)}/sq ft</Badge>
                              </div>
                              <p className="text-sm text-muted-foreground mb-3">{product.description}</p>
                              <div className="flex flex-wrap gap-1 mb-3">
                                {product.features.slice(0, 3).map((feature, i) => (
                                  <Badge key={i} variant="outline" className="text-xs">{feature}</Badge>
                                ))}
                              </div>
                              <div className="text-xs text-muted-foreground">
                                <span className="font-medium">Best for:</span>{' '}
                                {product.recommendedFor.join(', ')}
                              </div>
                            </div>
                          ))}
                        </div>
                      </AccordionContent>
                    </AccordionItem>
                  ))}
                </Accordion>
              </CardContent>
            </Card>

            {config.selectedProduct && (
              <Card className="border-primary">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg flex items-center gap-2">
                    <CheckCircle2 className="h-5 w-5 text-green-500" />
                    Selected Product
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="flex justify-between items-center">
                    <div>
                      <p className="font-semibold">{config.selectedProduct.name}</p>
                      <p className="text-sm text-muted-foreground">{config.selectedProduct.category}</p>
                    </div>
                    <div className="text-right">
                      <p className="font-semibold">${config.selectedProduct.basePricePerSqFt.toFixed(2)}</p>
                      <p className="text-sm text-muted-foreground">per sq ft</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            )}
          </div>
        );

      case 'design':
        return (
          <div className="space-y-6">
            {/* Patterns */}
            <Card>
              <CardHeader>
                <CardTitle className="text-lg flex items-center gap-2">
                  <Paintbrush className="h-5 w-5" />
                  Pattern Selection
                </CardTitle>
                <CardDescription>Choose a pattern for the surface design</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid gap-3 md:grid-cols-3">
                  <div
                    className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                      config.selectedPattern === null
                        ? 'border-primary bg-primary/5'
                        : 'border-transparent bg-muted/50 hover:border-primary/50'
                    }`}
                    onClick={() => updateConfig('selectedPattern', null)}
                  >
                    <div className="text-center">
                      <Circle className="h-6 w-6 mx-auto mb-2 text-muted-foreground" />
                      <p className="font-medium">No Pattern</p>
                      <p className="text-sm text-muted-foreground">$0.00/sq ft</p>
                    </div>
                  </div>
                  {patterns.map((pattern) => (
                    <div
                      key={pattern.id}
                      className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                        config.selectedPattern?.id === pattern.id
                          ? 'border-primary bg-primary/5'
                          : 'border-transparent bg-muted/50 hover:border-primary/50'
                      }`}
                      onClick={() => updateConfig('selectedPattern', pattern)}
                    >
                      <div className="flex justify-between items-start mb-2">
                        <h4 className="font-medium">{pattern.name}</h4>
                        <Badge variant="secondary">+${pattern.additionalCostPerSqFt.toFixed(2)}/sq ft</Badge>
                      </div>
                      <p className="text-sm text-muted-foreground mb-2">{pattern.description}</p>
                      <Badge variant="outline" className="text-xs">{pattern.complexity}</Badge>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Borders */}
            <Card>
              <CardHeader>
                <CardTitle className="text-lg">Border Selection</CardTitle>
                <CardDescription>Add a decorative border to enhance the design</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid gap-3 md:grid-cols-3">
                  <div
                    className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                      config.selectedBorder === null
                        ? 'border-primary bg-primary/5'
                        : 'border-transparent bg-muted/50 hover:border-primary/50'
                    }`}
                    onClick={() => updateConfig('selectedBorder', null)}
                  >
                    <div className="text-center">
                      <Circle className="h-6 w-6 mx-auto mb-2 text-muted-foreground" />
                      <p className="font-medium">No Border</p>
                      <p className="text-sm text-muted-foreground">$0.00/ln ft</p>
                    </div>
                  </div>
                  {borders.map((border) => (
                    <div
                      key={border.id}
                      className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                        config.selectedBorder?.id === border.id
                          ? 'border-primary bg-primary/5'
                          : 'border-transparent bg-muted/50 hover:border-primary/50'
                      }`}
                      onClick={() => updateConfig('selectedBorder', border)}
                    >
                      <div className="flex justify-between items-start mb-2">
                        <h4 className="font-medium">{border.name}</h4>
                        <Badge variant="secondary">+${border.additionalCostPerSqFt.toFixed(2)}/ln ft</Badge>
                      </div>
                      <p className="text-sm text-muted-foreground mb-2">{border.description}</p>
                      <Badge variant="outline" className="text-xs">{border.complexity}</Badge>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Logos */}
            <Card>
              <CardHeader>
                <CardTitle className="text-lg">Logo / Custom Artwork</CardTitle>
                <CardDescription>Add a logo or custom design element</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid gap-3 md:grid-cols-3">
                  <div
                    className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                      config.selectedLogo === null
                        ? 'border-primary bg-primary/5'
                        : 'border-transparent bg-muted/50 hover:border-primary/50'
                    }`}
                    onClick={() => updateConfig('selectedLogo', null)}
                  >
                    <div className="text-center">
                      <Circle className="h-6 w-6 mx-auto mb-2 text-muted-foreground" />
                      <p className="font-medium">No Logo</p>
                      <p className="text-sm text-muted-foreground">Standard installation</p>
                    </div>
                  </div>
                  {logos.map((logo) => (
                    <div
                      key={logo.id}
                      className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                        config.selectedLogo?.id === logo.id
                          ? 'border-primary bg-primary/5'
                          : 'border-transparent bg-muted/50 hover:border-primary/50'
                      }`}
                      onClick={() => updateConfig('selectedLogo', logo)}
                    >
                      <h4 className="font-medium mb-1">{logo.name}</h4>
                      <p className="text-sm text-muted-foreground mb-2">{logo.description}</p>
                      <Badge variant="outline" className="text-xs">{logo.complexity}</Badge>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>
        );

      case 'colors':
        return (
          <div className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="text-lg flex items-center gap-2">
                  <Palette className="h-5 w-5" />
                  Primary Color
                </CardTitle>
                <CardDescription>Select the main color for the surface</CardDescription>
              </CardHeader>
              <CardContent>
                <Tabs defaultValue="all">
                  <TabsList className="mb-4">
                    <TabsTrigger value="all">All Colors</TabsTrigger>
                    <TabsTrigger value="Earth Tones">Earth Tones</TabsTrigger>
                    <TabsTrigger value="Grays">Grays</TabsTrigger>
                    <TabsTrigger value="Blues">Blues</TabsTrigger>
                    <TabsTrigger value="Reds">Reds</TabsTrigger>
                  </TabsList>
                  {['all', 'Earth Tones', 'Grays', 'Blues', 'Reds'].map((category) => (
                    <TabsContent key={category} value={category}>
                      <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 gap-3">
                        {colorOptions
                          .filter(c => category === 'all' || c.category === category)
                          .map((color) => (
                            <div
                              key={color.id}
                              className={`p-2 rounded-lg border-2 cursor-pointer transition-all ${
                                config.primaryColor?.id === color.id
                                  ? 'border-primary'
                                  : 'border-transparent hover:border-primary/50'
                              }`}
                              onClick={() => updateConfig('primaryColor', color)}
                            >
                              <div
                                className="w-full aspect-square rounded-md mb-2 border shadow-sm"
                                style={{ backgroundColor: color.hex }}
                              />
                              <p className="text-xs font-medium text-center truncate">{color.name}</p>
                              {color.popularity === 'High' && (
                                <div className="flex justify-center mt-1">
                                  <Star className="h-3 w-3 text-yellow-500 fill-yellow-500" />
                                </div>
                              )}
                            </div>
                          ))}
                      </div>
                    </TabsContent>
                  ))}
                </Tabs>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle className="text-lg">Secondary Color (Optional)</CardTitle>
                <CardDescription>Add an accent or blend color</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 gap-3">
                  <div
                    className={`p-2 rounded-lg border-2 cursor-pointer transition-all ${
                      config.secondaryColor === null
                        ? 'border-primary bg-primary/5'
                        : 'border-transparent hover:border-primary/50'
                    }`}
                    onClick={() => updateConfig('secondaryColor', null)}
                  >
                    <div className="w-full aspect-square rounded-md mb-2 border-2 border-dashed flex items-center justify-center">
                      <span className="text-xs text-muted-foreground">None</span>
                    </div>
                    <p className="text-xs font-medium text-center">No Secondary</p>
                  </div>
                  {colorOptions.slice(0, 11).map((color) => (
                    <div
                      key={color.id}
                      className={`p-2 rounded-lg border-2 cursor-pointer transition-all ${
                        config.secondaryColor?.id === color.id
                          ? 'border-primary'
                          : 'border-transparent hover:border-primary/50'
                      }`}
                      onClick={() => updateConfig('secondaryColor', color)}
                    >
                      <div
                        className="w-full aspect-square rounded-md mb-2 border shadow-sm"
                        style={{ backgroundColor: color.hex }}
                      />
                      <p className="text-xs font-medium text-center truncate">{color.name}</p>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Color Preview */}
            {(config.primaryColor || config.secondaryColor) && (
              <Card className="border-primary">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg flex items-center gap-2">
                    <CheckCircle2 className="h-5 w-5 text-green-500" />
                    Color Preview
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="flex items-center gap-4">
                    {config.primaryColor && (
                      <div className="flex items-center gap-2">
                        <div
                          className="w-10 h-10 rounded-md border shadow-sm"
                          style={{ backgroundColor: config.primaryColor.hex }}
                        />
                        <div>
                          <p className="font-medium">{config.primaryColor.name}</p>
                          <p className="text-xs text-muted-foreground">Primary</p>
                        </div>
                      </div>
                    )}
                    {config.secondaryColor && (
                      <>
                        <span className="text-muted-foreground">+</span>
                        <div className="flex items-center gap-2">
                          <div
                            className="w-10 h-10 rounded-md border shadow-sm"
                            style={{ backgroundColor: config.secondaryColor.hex }}
                          />
                          <div>
                            <p className="font-medium">{config.secondaryColor.name}</p>
                            <p className="text-xs text-muted-foreground">Secondary</p>
                          </div>
                        </div>
                      </>
                    )}
                  </div>
                </CardContent>
              </Card>
            )}
          </div>
        );

      case 'texture':
        return (
          <div className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="text-lg flex items-center gap-2">
                  <Droplets className="h-5 w-5" />
                  Surface Texture Options
                </CardTitle>
                <CardDescription>Select the texture profile for the surface</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid gap-4 md:grid-cols-3">
                  {textureOptions.map((texture) => (
                    <div
                      key={texture.id}
                      className={`p-6 rounded-lg border-2 cursor-pointer transition-all ${
                        config.selectedTexture?.id === texture.id
                          ? 'border-primary bg-primary/5'
                          : 'border-transparent bg-muted/50 hover:border-primary/50'
                      }`}
                      onClick={() => updateConfig('selectedTexture', texture)}
                    >
                      <div className="flex items-center gap-3 mb-4">
                        <div className="w-12 h-12 rounded-lg bg-gradient-to-b from-primary/20 to-primary/60 flex items-center justify-center">
                          <span className="text-lg font-bold">{texture.code}</span>
                        </div>
                        <div>
                          <h4 className="font-semibold">{texture.name}</h4>
                          <p className="text-sm text-muted-foreground">{texture.code}</p>
                        </div>
                      </div>
                      <p className="text-sm text-muted-foreground mb-4">{texture.description}</p>
                      <div className="space-y-2">
                        <div className="flex justify-between text-sm">
                          <span className="text-muted-foreground">Slip Resistance:</span>
                          <Badge variant={texture.slipResistance === 'High' ? 'default' : 'secondary'}>
                            {texture.slipResistance}
                          </Badge>
                        </div>
                        <div className="flex justify-between text-sm">
                          <span className="text-muted-foreground">Maintenance:</span>
                          <Badge variant="outline">{texture.maintenanceLevel}</Badge>
                        </div>
                      </div>
                      <Separator className="my-4" />
                      <div>
                        <p className="text-xs font-medium mb-2">Best For:</p>
                        <div className="flex flex-wrap gap-1">
                          {texture.bestFor.map((use, i) => (
                            <Badge key={i} variant="outline" className="text-xs">{use}</Badge>
                          ))}
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {config.selectedTexture && (
              <Card className="border-primary">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg flex items-center gap-2">
                    <CheckCircle2 className="h-5 w-5 text-green-500" />
                    Selected Texture
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="flex items-center gap-4">
                    <div className="w-16 h-16 rounded-lg bg-gradient-to-b from-primary/20 to-primary/60 flex items-center justify-center">
                      <span className="text-2xl font-bold">{config.selectedTexture.code}</span>
                    </div>
                    <div>
                      <p className="font-semibold text-lg">{config.selectedTexture.name}</p>
                      <p className="text-sm text-muted-foreground">{config.selectedTexture.description}</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            )}
          </div>
        );

      case 'topcoat':
        return (
          <div className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="text-lg flex items-center gap-2">
                  <Shield className="h-5 w-5" />
                  Top Coat Options
                </CardTitle>
                <CardDescription>Select additional performance coating</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid gap-4 md:grid-cols-2">
                  {topCoatOptions.map((topCoat) => (
                    <div
                      key={topCoat.id}
                      className={`p-5 rounded-lg border-2 cursor-pointer transition-all ${
                        config.selectedTopCoat?.id === topCoat.id
                          ? 'border-primary bg-primary/5'
                          : 'border-transparent bg-muted/50 hover:border-primary/50'
                      }`}
                      onClick={() => updateConfig('selectedTopCoat', topCoat)}
                    >
                      <div className="flex justify-between items-start mb-3">
                        <h4 className="font-semibold">{topCoat.name}</h4>
                        <Badge variant="secondary">+${topCoat.additionalCostPerSqFt.toFixed(2)}/sq ft</Badge>
                      </div>
                      <p className="text-sm text-muted-foreground mb-4">{topCoat.description}</p>
                      <div className="grid grid-cols-3 gap-2 text-sm">
                        <div>
                          <p className="text-muted-foreground text-xs">Durability</p>
                          <Badge variant="outline" className="mt-1">{topCoat.durability}</Badge>
                        </div>
                        <div>
                          <p className="text-muted-foreground text-xs">UV Resist.</p>
                          <Badge variant="outline" className="mt-1">{topCoat.uvResistance}</Badge>
                        </div>
                        <div>
                          <p className="text-muted-foreground text-xs">Chem. Resist.</p>
                          <Badge variant="outline" className="mt-1">{topCoat.chemicalResistance}</Badge>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {config.selectedTopCoat && (
              <Card className="border-primary">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg flex items-center gap-2">
                    <CheckCircle2 className="h-5 w-5 text-green-500" />
                    Selected Top Coat
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="flex justify-between items-center">
                    <div>
                      <p className="font-semibold">{config.selectedTopCoat.name}</p>
                      <p className="text-sm text-muted-foreground">{config.selectedTopCoat.description}</p>
                    </div>
                    <div className="text-right">
                      <p className="font-semibold">+${config.selectedTopCoat.additionalCostPerSqFt.toFixed(2)}</p>
                      <p className="text-sm text-muted-foreground">per sq ft</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            )}
          </div>
        );

      case 'summary':
        return (
          <div className="space-y-6">
            {/* Project Summary */}
            <Card>
              <CardHeader>
                <CardTitle className="text-lg flex items-center gap-2">
                  <FileText className="h-5 w-5" />
                  Project Summary
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid gap-4 md:grid-cols-2">
                  <div className="space-y-3">
                    <div>
                      <p className="text-sm text-muted-foreground">Customer</p>
                      <p className="font-medium">{config.customerName || 'Not specified'}</p>
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Address</p>
                      <p className="font-medium">{config.projectAddress || 'Not specified'}</p>
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Square Footage</p>
                      <p className="font-medium">{config.squareFootage.toLocaleString()} sq ft</p>
                    </div>
                  </div>
                  <div className="space-y-3">
                    <div>
                      <p className="text-sm text-muted-foreground">Location Type</p>
                      <p className="font-medium">
                        {locationFactors.find(l => l.id === config.locationType)?.name || 'Not specified'}
                      </p>
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Performance Priority</p>
                      <p className="font-medium capitalize">{config.performancePriority || 'Not specified'}</p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Configuration Summary */}
            <Card>
              <CardHeader>
                <CardTitle className="text-lg">Configuration Details</CardTitle>
              </CardHeader>
              <CardContent>
                <ScrollArea className="h-[300px] pr-4">
                  <div className="space-y-4">
                    {/* System */}
                    <div className="flex justify-between items-start p-3 rounded-lg bg-muted/50">
                      <div>
                        <p className="font-medium">Product System</p>
                        <p className="text-sm text-muted-foreground">
                          {config.selectedProduct?.name || 'Not selected'}
                        </p>
                      </div>
                      {config.selectedProduct && (
                        <p className="font-semibold">${config.selectedProduct.basePricePerSqFt.toFixed(2)}/sq ft</p>
                      )}
                    </div>

                    {/* Design */}
                    <div className="flex justify-between items-start p-3 rounded-lg bg-muted/50">
                      <div>
                        <p className="font-medium">Design Options</p>
                        <div className="text-sm text-muted-foreground space-y-1">
                          <p>Pattern: {config.selectedPattern?.name || 'None'}</p>
                          <p>Border: {config.selectedBorder?.name || 'None'}</p>
                          <p>Logo: {config.selectedLogo?.name || 'None'}</p>
                        </div>
                      </div>
                      <div className="text-right text-sm">
                        {config.selectedPattern && (
                          <p>+${config.selectedPattern.additionalCostPerSqFt.toFixed(2)}/sq ft</p>
                        )}
                        {config.selectedBorder && (
                          <p>+${config.selectedBorder.additionalCostPerSqFt.toFixed(2)}/ln ft</p>
                        )}
                      </div>
                    </div>

                    {/* Colors */}
                    <div className="flex justify-between items-start p-3 rounded-lg bg-muted/50">
                      <div>
                        <p className="font-medium">Colors</p>
                        <div className="flex items-center gap-2 mt-1">
                          {config.primaryColor && (
                            <div className="flex items-center gap-1">
                              <div
                                className="w-5 h-5 rounded border"
                                style={{ backgroundColor: config.primaryColor.hex }}
                              />
                              <span className="text-sm">{config.primaryColor.name}</span>
                            </div>
                          )}
                          {config.secondaryColor && (
                            <>
                              <span className="text-muted-foreground">+</span>
                              <div className="flex items-center gap-1">
                                <div
                                  className="w-5 h-5 rounded border"
                                  style={{ backgroundColor: config.secondaryColor.hex }}
                                />
                                <span className="text-sm">{config.secondaryColor.name}</span>
                              </div>
                            </>
                          )}
                          {!config.primaryColor && !config.secondaryColor && (
                            <span className="text-sm text-muted-foreground">Not selected</span>
                          )}
                        </div>
                      </div>
                    </div>

                    {/* Texture */}
                    <div className="flex justify-between items-start p-3 rounded-lg bg-muted/50">
                      <div>
                        <p className="font-medium">Surface Texture</p>
                        <p className="text-sm text-muted-foreground">
                          {config.selectedTexture
                            ? `${config.selectedTexture.code} - ${config.selectedTexture.name}`
                            : 'Not selected'}
                        </p>
                      </div>
                      {config.selectedTexture && (
                        <Badge variant="outline">{config.selectedTexture.slipResistance} Slip</Badge>
                      )}
                    </div>

                    {/* Top Coat */}
                    <div className="flex justify-between items-start p-3 rounded-lg bg-muted/50">
                      <div>
                        <p className="font-medium">Top Coat</p>
                        <p className="text-sm text-muted-foreground">
                          {config.selectedTopCoat?.name || 'Not selected'}
                        </p>
                      </div>
                      {config.selectedTopCoat && (
                        <p className="font-semibold">+${config.selectedTopCoat.additionalCostPerSqFt.toFixed(2)}/sq ft</p>
                      )}
                    </div>
                  </div>
                </ScrollArea>
              </CardContent>
            </Card>

            {/* Cost Estimate */}
            {estimate && (
              <Card className="border-primary">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg flex items-center gap-2">
                    <Calculator className="h-5 w-5" />
                    Estimated Cost
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    <div className="flex justify-between text-sm">
                      <span className="text-muted-foreground">Base Product</span>
                      <span>${estimate.breakdown.product.toFixed(2)}/sq ft</span>
                    </div>
                    {estimate.breakdown.pattern > 0 && (
                      <div className="flex justify-between text-sm">
                        <span className="text-muted-foreground">Pattern</span>
                        <span>+${estimate.breakdown.pattern.toFixed(2)}/sq ft</span>
                      </div>
                    )}
                    {estimate.breakdown.topCoat > 0 && (
                      <div className="flex justify-between text-sm">
                        <span className="text-muted-foreground">Top Coat</span>
                        <span>+${estimate.breakdown.topCoat.toFixed(2)}/sq ft</span>
                      </div>
                    )}
                    <Separator />
                    <div className="flex justify-between">
                      <span className="font-medium">Price per sq ft</span>
                      <span className="font-semibold">${estimate.perSqFt.toFixed(2)}</span>
                    </div>
                    <div className="flex justify-between items-center p-4 rounded-lg bg-primary/10">
                      <span className="font-semibold text-lg">Total Estimate</span>
                      <span className="font-bold text-2xl text-primary">
                        ${estimate.baseCost.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                      </span>
                    </div>
                  </div>
                </CardContent>
              </Card>
            )}

            {/* Actions */}
            <div className="flex flex-wrap gap-3">
              <Button onClick={copyToClipboard} className="flex-1">
                {copied ? (
                  <>
                    <Check className="h-4 w-4 mr-2" />
                    Copied!
                  </>
                ) : (
                  <>
                    <Copy className="h-4 w-4 mr-2" />
                    Copy Quote
                  </>
                )}
              </Button>
              <Button variant="outline" onClick={handleReset} className="flex-1">
                <RefreshCw className="h-4 w-4 mr-2" />
                Start New Quote
              </Button>
            </div>

            {config.projectNotes && (
              <Card>
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg">Project Notes</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-muted-foreground whitespace-pre-wrap">{config.projectNotes}</p>
                </CardContent>
              </Card>
            )}
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-950 dark:to-slate-900">
      {/* Header */}
      <header className="sticky top-0 z-50 bg-white/80 dark:bg-slate-900/80 backdrop-blur-sm border-b">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-orange-500 to-red-600 flex items-center justify-center">
                <Shield className="h-6 w-6 text-white" />
              </div>
              <div>
                <h1 className="font-bold text-xl">TCP Sales Tool</h1>
                <p className="text-xs text-muted-foreground">The Concrete Protector</p>
              </div>
            </div>
            <div className="flex items-center gap-4">
              <div className="text-right hidden sm:block">
                <p className="text-sm text-muted-foreground">Progress</p>
                <p className="font-semibold">{Math.round(progress)}%</p>
              </div>
              <Progress value={progress} className="w-24 sm:w-32" />
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-6">
        <div className="grid gap-6 lg:grid-cols-[280px_1fr]">
          {/* Sidebar - Steps Navigation */}
          <Card className="lg:sticky lg:top-24 lg:h-fit">
            <CardHeader className="pb-3">
              <CardTitle className="text-base">Sales Process</CardTitle>
              <CardDescription>
                {completedSteps.length} of {steps.length} steps completed
              </CardDescription>
            </CardHeader>
            <CardContent className="p-0">
              <nav className="space-y-1 px-3 pb-3">
                {steps.map((step, index) => {
                  const Icon = step.icon;
                  const isActive = currentStep === index;
                  const isCompleted = completedSteps.includes(step.id);
                  
                  return (
                    <button
                      key={step.id}
                      onClick={() => setCurrentStep(index)}
                      className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-left transition-all ${
                        isActive
                          ? 'bg-primary text-primary-foreground'
                          : isCompleted
                          ? 'bg-primary/10 text-primary hover:bg-primary/20'
                          : 'hover:bg-muted'
                      }`}
                    >
                      <div className={`flex-shrink-0 w-6 h-6 rounded-full flex items-center justify-center ${
                        isActive
                          ? 'bg-primary-foreground/20'
                          : isCompleted
                          ? 'bg-primary/20'
                          : 'bg-muted'
                      }`}>
                        {isCompleted ? (
                          <CheckCircle2 className="h-4 w-4" />
                        ) : (
                          <Icon className="h-3.5 w-3.5" />
                        )}
                      </div>
                      <span className="text-sm font-medium">{step.title}</span>
                    </button>
                  );
                })}
              </nav>
            </CardContent>
          </Card>

          {/* Main Content Area */}
          <div className="space-y-4">
            {/* Step Header */}
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                {(() => {
                  const Icon = steps[currentStep].icon;
                  return <Icon className="h-5 w-5 text-primary" />;
                })()}
                <h2 className="text-xl font-semibold">{steps[currentStep].title}</h2>
              </div>
              <Badge variant="outline">
                Step {currentStep + 1} of {steps.length}
              </Badge>
            </div>

            {/* Step Content */}
            {renderStepContent()}

            {/* Navigation Buttons */}
            <div className="flex justify-between pt-4">
              <Button
                variant="outline"
                onClick={handlePrev}
                disabled={currentStep === 0}
              >
                <ArrowLeft className="h-4 w-4 mr-2" />
                Previous
              </Button>
              <Button
                onClick={handleNext}
                disabled={currentStep === steps.length - 1}
              >
                Next
                <ArrowRight className="h-4 w-4 ml-2" />
              </Button>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="mt-auto border-t bg-white/80 dark:bg-slate-900/80 backdrop-blur-sm">
        <div className="container mx-auto px-4 py-4">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-2 text-sm text-muted-foreground">
            <p>Sales Tool for The Concrete Protector Contractors</p>
            <p>Products • Equipment • Training</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
