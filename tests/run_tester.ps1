# Tiny Hearts - Tester Agent Launcher
$PythonPath = "C:\Users\jonat\AppData\Local\Programs\Python\Python314\python.exe"
$ScriptPath = Join-Path $PSScriptRoot "tester_agent.py"

Write-Host "Iniciando Tiny Hearts Tester Agent..." -ForegroundColor Cyan
& $PythonPath $ScriptPath
