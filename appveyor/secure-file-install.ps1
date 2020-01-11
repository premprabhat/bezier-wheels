# From: https://raw.githubusercontent.com/appveyor/secure-file/5163b6ef52c015159d7c9f204a8b1e365422d010/install.ps1
$ProgressPreference='SilentlyContinue'

$tempdir = Join-Path $([System.IO.Path]::GetTempPath()) $([System.Guid]::NewGuid())
New-Item -ItemType Directory -Path $tempdir

# BEGIN: Modified section
#   WAS: $zipPath = Join-Path $tempdir 'secure-file.zip'
#   WAS: [Net.ServicePointManager]::SecurityProtocol = "tls12, tls11, tls"
#   WAS: (New-Object Net.WebClient).DownloadFile('https://github.com/appveyor/secure-file/releases/download/1.0.0/secure-file.zip', $zipPath)
$zipPath = './appveyor/secure-file.zip' # New code
#   END: Modified section
Expand-Archive $zipPath -DestinationPath (Join-Path (pwd).path "appveyor-tools") -Force
if ($isLinux) {
	chmod +x ./appveyor-tools/secure-file
}
del $tempdir -Recurse -Force
