Imports ESRI.ArcGIS.Carto
Imports ESRI.ArcGIS.Geometry

Public Class Form1
Private m_pDoc As IMapDocument

Private Sub Button1_Click(ByVal sender As System.Object, _
ByVal e As System.EventArgs) Handles Button1.Click

CreateMXD()
AddRectangle()
SaveDoc()
MessageBox.Show("Done")
m_pDoc = Nothing
Me.Close()
End Sub

Private Sub CreateMXD()
Dim aDoc As IMapDocument = Nothing
'Create a new MXD Document
Try
While aDoc Is Nothing
aDoc = New MapDocument
End While
Catch ex As Exception
MessageBox.Show(ex.Message, "Error")
End Try
aDoc.Open(Me.tbxOpen.Text)
m_pDoc = aDoc
End Sub

Private Sub AddRectangle()
'Adds a graphic element to the layout
Dim pPageLayout As IPageLayout
Dim pContainer As IGraphicsContainer
Dim pGraphicElement As IElement
Dim pEnvelope As IEnvelope
'Specify where to put the rectangle (on the page layout)
pPageLayout = m_pDoc.PageLayout
pContainer = pPageLayout
'Create a rectangle

'If you wanted to get fancy, you could change the symbology here
pGraphicElement = New RectangleElement
pEnvelope = New Envelope
pEnvelope.XMax = 8
pEnvelope.XMin = 0.5
pEnvelope.YMax = 8
pEnvelope.YMin = 0.5
pGraphicElement.Geometry = pEnvelope

'Add the rectangle to the page layout
pContainer.AddElement(pGraphicElement, 0)
End Sub

Private Sub SaveDoc()
'Save the MXD document
m_pDoc.SaveAs(Me.tbxSaveAs.Text)
End Sub

End Class