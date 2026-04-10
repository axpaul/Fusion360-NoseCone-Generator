import adsk.core, adsk.fusion, traceback
import math

# --- LOGIQUE MATHÉMATIQUE ---
def calculate_y(type_ogive, x, L, R):
    if type_ogive == 'Tangent':
        rho = (R**2 + L**2) / (2 * R)
        return math.sqrt(max(0, rho**2 - (L - x)**2)) + R - rho
    elif type_ogive == 'Parabolic':
        return R * ((2*(x/L)) - (x/L)**2)
    elif type_ogive == 'Von Karman':
        theta = math.acos(1 - (2 * x / L))
        return (R / math.sqrt(math.pi)) * math.sqrt(theta - math.sin(2 * theta) / 2)
    elif type_ogive == 'Conic':
        return x * (R / L)
    elif type_ogive == 'Elliptical':
        return R * math.sqrt(max(0, 1 - ((L - x)**2 / L**2)))
    return 0

# --- GESTION DE L'INTERFACE ---
class NoseConeCommandExecuteHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            command = args.firingEvent.sender
            inputs = command.commandInputs

            # Récupération des valeurs de l'UI
            type_sel = inputs.itemById('type_ogive').selectedItem.name
            L_val = inputs.itemById('longueur').value 
            D_val = inputs.itemById('diametre').value
            # CORRECTION ICI : .valueOne pour le Slider
            nb_pts = int(inputs.itemById('nb_points').valueOne)
            R_val = D_val / 2

            app = adsk.core.Application.get()
            design = adsk.fusion.Design.cast(app.activeProduct)
            rootComp = design.rootComponent
            
            sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
            sketch.name = f"Ogive_{type_sel}_{int(L_val*10)}mm"
            
            points = adsk.core.ObjectCollection.create()
            for i in range(nb_pts + 1):
                x = (L_val / nb_pts) * i
                y = calculate_y(type_sel, x, L_val, R_val)
                points.add(adsk.core.Point3D.create(x, y, 0))

            sketch.sketchCurves.sketchFittedSplines.add(points)
            
            lines = sketch.sketchCurves.sketchLines
            p0 = adsk.core.Point3D.create(0, 0, 0)
            pL = adsk.core.Point3D.create(L_val, 0, 0)
            lines.addByTwoPoints(points.item(0), p0)
            lines.addByTwoPoints(p0, pL)
            lines.addByTwoPoints(pL, points.item(points.count - 1))
            
            app.activeViewport.fit()
        except:
            adsk.core.Application.get().userInterface.messageBox(traceback.format_exc())

class NoseConeCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            cmd = args.command
            inputs = cmd.commandInputs

            # UI : Liste déroulante
            drop = inputs.addDropDownCommandInput('type_ogive', 'Type d\'ogive', adsk.core.DropDownStyles.LabeledIconDropDownStyle)
            drop.listItems.add('Tangent', True)
            drop.listItems.add('Parabolic', False)
            drop.listItems.add('Von Karman', False)
            drop.listItems.add('Conic', False)
            drop.listItems.add('Elliptical', False)

            # UI : Dimensions
            inputs.addValueInput('longueur', 'Longueur', 'mm', adsk.core.ValueInput.createByReal(15))
            inputs.addValueInput('diametre', 'Diamètre', 'mm', adsk.core.ValueInput.createByReal(4))
            
            # UI : Slider (Nb de points)
            slider = inputs.addIntegerSliderCommandInput('nb_points', 'Précision (points)', 2, 100, False)
            slider.valueOne = 40

            # Connection des événements
            onExecute = NoseConeCommandExecuteHandler()
            cmd.execute.add(onExecute)
            handlers.append(onExecute)
        except:
            adsk.core.Application.get().userInterface.messageBox(traceback.format_exc())

handlers = []

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        cmdDef = ui.commandDefinitions.itemById('NoseConeGenV2')
        if cmdDef:
            cmdDef.deleteMe()
        
        cmdDef = ui.commandDefinitions.addButtonDefinition('NoseConeGenV2', 'Générateur d\'Ogive', 'Crée un profil d\'ogive')

        onCommandCreated = NoseConeCommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        handlers.append(onCommandCreated)

        cmdDef.execute()
        adsk.autoTerminate(False)
    except:
        if ui:
            ui.messageBox('Erreur :\n{}'.format(traceback.format_exc()))