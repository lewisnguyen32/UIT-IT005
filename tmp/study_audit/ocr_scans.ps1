$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Runtime.WindowsRuntime
[Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType=WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime] | Out-Null
[Windows.Storage.Streams.IRandomAccessStream, Windows.Storage.Streams, ContentType=WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType=WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics.Imaging, ContentType=WindowsRuntime] | Out-Null
$script:asTask = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' } | Select-Object -First 1
function Await-WinRT($Operation, $ResultType) {
    $task = $script:asTask.MakeGenericMethod($ResultType).Invoke($null, @($Operation))
    $task.GetAwaiter().GetResult()
}
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
if ($null -eq $engine) { throw 'No installed OCR engine language.' }
Write-Output ('OCR language: ' + $engine.RecognizerLanguage.LanguageTag)
foreach ($sid in @('E01','E02')) {
    $dest=Join-Path $PSScriptRoot ('visuals\'+$sid)
    $blocks=New-Object System.Collections.Generic.List[string]
    foreach ($png in Get-ChildItem -LiteralPath $dest -Filter 'page-*.png' | Sort-Object Name) {
        $file=Await-WinRT ([Windows.Storage.StorageFile]::GetFileFromPathAsync($png.FullName)) ([Windows.Storage.StorageFile])
        $stream=Await-WinRT ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
        $decoder=Await-WinRT ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
        $bitmap=Await-WinRT ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
        $result=Await-WinRT ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
        $blocks.Add("`n`n===== OCR $($png.BaseName) =====`n")
        foreach ($line in $result.Lines) { $blocks.Add($line.Text) }
        $bitmap.Dispose()
        $stream.Dispose()
        Write-Output ($sid + ' ' + $png.BaseName + ' lines=' + $result.Lines.Count)
    }
    [System.IO.File]::WriteAllText((Join-Path $PSScriptRoot ($sid+'_ocr.txt')), [string]::Join("`n",$blocks), (New-Object System.Text.UTF8Encoding($false)))
}
