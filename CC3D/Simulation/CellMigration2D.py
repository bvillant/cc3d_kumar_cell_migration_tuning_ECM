from cc3d import CompuCellSetup

from CellMigration2DSteppables import CellMigration2DSteppable

CompuCellSetup.register_steppable(steppable=CellMigration2DSteppable(frequency=1))

from CellMigration2DSteppables import PolarityEvolutionSteppable

CompuCellSetup.register_steppable(steppable=PolarityEvolutionSteppable(frequency=1))

from CellMigration2DSteppables import MMPSecretionSteppable

CompuCellSetup.register_steppable(steppable=MMPSecretionSteppable(frequency=1))

from CellMigration2DSteppables import ECMDegradationSteppable

CompuCellSetup.register_steppable(steppable=ECMDegradationSteppable(frequency=1))

from CellMigration2DSteppables import IdFieldVisualizationSteppable

CompuCellSetup.register_steppable(steppable=IdFieldVisualizationSteppable(frequency=1))

CompuCellSetup.run()

        
        
