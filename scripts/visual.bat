@Echo visial.exe script for Arcgis
@if not %4 == "true" goto skip
@if not %5 == "#" goto buffer

@Echo no optional parameters passed
@Echo begining visual.exe
@Z:\svn\SOM_PAK\visual.exe -din %1 -cin %2 -dout %3
@goto end

:skip
@if not %5 == "#" goto skipbuffer
@Echo vector no skip mode 
@Echo begining visual.exe
@Z:\svn\SOM_PAK\visual.exe -din %1 -cin %2 -dout %3 -noskip
@goto end

:buffer
@Echo read buffer mode
@Echo begining visual.exe
@Z:\svn\SOM_PAK\visual.exe -din %1 -cin %2 -dout %3 -buffer %5
@goto end

:skipbuffer
@Echo vector no skip and read buffer mode
@Echo begining visual.exe
@Z:\svn\SOM_PAK\visual.exe -din %1 -cin %2 -dout %3 -noskip -buffer %5
@goto end

:end 
