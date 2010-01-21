<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
                version="1.0">

<xsl:import href = "default.xsl" />
<xsl:output method="html"/>

<!-- Overwrite Select Templates -->
<xsl:template match="PropertyGroup">
    <TR valign="top"><TD>
        <DIV ID="GEN" STYLE="cursor: hand;">
            <!-- Process required parameters -->
            <xsl:for-each select="Property"> 
                <xsl:choose>
                    <xsl:when test='not(contains(PropertyLabel,"(optional)"))'>
                        <xsl:apply-templates select="." />
                    </xsl:when>
                </xsl:choose>
            </xsl:for-each>

            <!-- Add expanding section for optional parameters -->
            <TABLE onclick="parent.clicker({PropertyGroupName},{PropertyGroupName}Image);" STYLE="cursor:hand;" border="0" cellspacing="0" cellpadding="0" width="94%">                
<TR valign="top" bgcolor="menu">
                    <TD colspan="2">
                        <TABLE border="0" width="100%" cellpadding="0" cellspacing="0">
                            <TR bgcolor="menu">
                                <TH align="left">
  <IMG ID="{PropertyGroupName}Image" SRC="{../../CommonPath}/triangle.gif" ALT="*" ALIGN="MIDDLE" BORDER="0" WIDTH="11" HEIGHT="11"/>
                                    <SPAN class="caption" STYLE="color:menutext;">Click to Show Optional Parameters</SPAN>
                                </TH>
                            </TR>
                        </TABLE>
                    </TD>
                </TR>
                <TR valign="top">
                    <TD colspan="2">
                        <DIV ID="{PropertyGroupName}" STYLE="display:'none';" onclick="window.event.cancelBubble = true;">
                            <TABLE border="0" cellspacing="1" cellpadding="4" width="90%">
                                <xsl:for-each select="Property"> 
                                    <xsl:choose>
                                        <xsl:when test='contains(PropertyLabel,"(optional)")'>
                                            <xsl:apply-templates select="." />
                                        </xsl:when>
                                    </xsl:choose>
                                </xsl:for-each> 
                            </TABLE>
                        </DIV>
                    </TD>
                </TR>
            </TABLE>
        </DIV>
    </TD></TR>
</xsl:template>
</xsl:stylesheet>
