$projectRoot = Split-Path -Parent $PSScriptRoot
$buildDirectory = Join-Path $projectRoot 'build'
$chapterNames = @(
    'chapter01_formulations',
    'chapter02_mechanism',
    'chapter03_coordinates',
    'chapter04_lagrange_double_pendulum',
    'chapter05_loop_constraints',
    'chapter06_constraint_kinematics',
    'chapter07_constrained_dynamics',
    'chapter08_initial_conditions',
    'chapter09_integration_and_drift',
    'chapter10_verification',
    'chapter11_results',
    'chapter12_limitations'
)

Push-Location $projectRoot
try {
    New-Item -ItemType Directory -Path $buildDirectory -Force | Out-Null

    foreach ($chapterName in $chapterNames) {
        $source = "chapters\$chapterName.tex"
        & pdflatex -output-directory=build -interaction=nonstopmode -halt-on-error $source *> $null
        if ($LASTEXITCODE -ne 0) { throw "pdfLaTeX failed for $chapterName" }

        & bibtex "build\$chapterName" *> $null
        if ($LASTEXITCODE -ne 0) { throw "BibTeX failed for $chapterName" }

        & pdflatex -output-directory=build -interaction=nonstopmode -halt-on-error $source *> $null
        if ($LASTEXITCODE -ne 0) { throw "Second pdfLaTeX pass failed for $chapterName" }

        & pdflatex -output-directory=build -interaction=nonstopmode -halt-on-error $source *> $null
        if ($LASTEXITCODE -ne 0) { throw "Final pdfLaTeX pass failed for $chapterName" }

        $logPath = Join-Path $buildDirectory "$chapterName.log"
        $warnings = Select-String -Path $logPath -Pattern 'Citation .*undefined|Reference .*undefined|Overfull \\hbox|Fatal error'
        if ($warnings) {
            Write-Output "WARN $chapterName"
            $warnings | ForEach-Object { Write-Output $_.Line }
        }
        else {
            Write-Output "PASS $chapterName"
        }
    }

    & pdflatex -output-directory=build -interaction=nonstopmode -halt-on-error main.tex *> $null
    if ($LASTEXITCODE -ne 0) { throw 'Initial master pdfLaTeX pass failed' }

    & bibtex build\main *> $null
    if ($LASTEXITCODE -ne 0) { throw 'Master BibTeX pass failed' }

    & pdflatex -output-directory=build -interaction=nonstopmode -halt-on-error main.tex *> $null
    if ($LASTEXITCODE -ne 0) { throw 'Second master pdfLaTeX pass failed' }

    & pdflatex -output-directory=build -interaction=nonstopmode -halt-on-error main.tex *> $null
    if ($LASTEXITCODE -ne 0) { throw 'Final master pdfLaTeX pass failed' }

    $masterLog = Join-Path $buildDirectory 'main.log'
    $masterWarnings = Select-String -Path $masterLog -Pattern 'Citation .*undefined|Reference .*undefined|duplicate ignored|Overfull \\hbox|Fatal error'
    if ($masterWarnings) {
        Write-Output 'WARN main'
        $masterWarnings | ForEach-Object { Write-Output $_.Line }
    }
    else {
        Write-Output 'PASS main'
    }
}
finally {
    Pop-Location
}