import vtk

sphere = vtk.vtkSphereSource()
sphere.SetRadius(1)
sphere.SetCenter(0, 0, 0)
sphere.SetThetaResolution(360)
sphere.SetPhiResolution(360)
sphere.Update()

sphere_property = vtk.vtkProperty()
sphere_property.SetOpacity(0.5)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(sphere.GetOutputPort())
mapper.SetScalarVisibility(True)
mapper.Update()

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetOpacity(sphere_property.GetOpacity())

writer = vtk.vtkPolyDataWriter()
writer.SetInputData(sphere.GetOutput())
writer.SetFileName('mysphere.vtk')
writer.Update()