$KaliIP = "172.20.10.8"
$CertUrl = "http://${KaliIP}:8000/mitmproxy-ca-cert.cer"
$LocalCertPath = "$env:TEMP\mitmproxy-ca-cert.cer"

# Remove old lab certificates
Get-ChildItem Cert:\LocalMachine\Root | Where-Object { $_.Subject -like "*mitmproxy*" } | Remove-Item

# Download and import certificate
Invoke-WebRequest -Uri $CertUrl -OutFile $LocalCertPath
Import-Certificate -FilePath $LocalCertPath -CertStoreLocation "Cert:\LocalMachine\Root"
