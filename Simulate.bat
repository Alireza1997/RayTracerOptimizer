
@echo off

set Program=C:\Takahiro\Programs\RayTubeTracing\3\x64\Release\RayTubeTracing.exe

echo;
echo '%0' started by %USERNAME% @ %COMPUTERNAME%: %DATE% %TIME%
echo current directory: '%CD%'
echo program file: '%Program%'

echo;

%Program%

echo;

echo '%0' finished: %DATE% %TIME%
echo;

