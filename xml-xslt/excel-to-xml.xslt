<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
  xmlns:o="urn:schemas-microsoft-com:office:office"
  xmlns:x="urn:schemas-microsoft-com:office:excel"
  xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"
  xmlns:html="http://www.w3.org/TR/REC-html40" exclude-result-prefixes="o x ss html">
<xsl:output omit-xml-declaration="no" method="xml" version="1.0" encoding="UTF-16" indent="yes" standalone="no"  doctype-system="concept.dtd" doctype-public="-//OASIS//DTD DITA Concept//EN"/>
<xsl:strip-space elements="*"/>
<xsl:template match="ss:*">
  <xsl:for-each select="ss:Worksheet/ss:Table/ss:Row[position() > 1]">
    <xsl:result-document href="output/section{position()}.html"><concept xml:lang="en-GB"> 
  <title><xsl:value-of select="ss:Cell[1]/ss:Data"/></title>
  <shortdesc>
        <xsl:choose>
          <xsl:when test="ss:Cell[7]/ss:Data != ''">
            <xsl:value-of select="ss:Cell[7]/ss:Data"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="ss:Cell[@ss:Index=7]/ss:Data"/>
          </xsl:otherwise>
        </xsl:choose>
  </shortdesc> 
  <prolog>
    <metadata>
      <keywords>
        <indexterm />
      </keywords>
    </metadata>
  </prolog> 
  <conbody>
    <section>
      <title>my title</title>
      <p>
        <xsl:choose>
          <xsl:when test="ss:Cell[7]/ss:Data != ''">
            <xsl:value-of select="ss:Cell[7]/ss:Data"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="ss:Cell[@ss:Index=7]/ss:Data"/>
          </xsl:otherwise>
        </xsl:choose>
      </p>
    </section>
    <section>
      <title>my title</title>
      <p>
        <xsl:choose>
          <xsl:when test="ss:Cell[13]/ss:Data != ''">
            <xsl:value-of select="ss:Cell[13]/ss:Data"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="ss:Cell[@ss:Index=13]/ss:Data"/>
          </xsl:otherwise>
        </xsl:choose>
      </p>
    </section>
    <section>
      <title>my title</title>
      <p>
        <xsl:choose>
          <xsl:when test="ss:Cell[15]/ss:Data != ''">
            <xsl:value-of select="ss:Cell[15]/ss:Data"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="ss:Cell[@ss:Index=15]/ss:Data"/>
          </xsl:otherwise>
        </xsl:choose>
      </p>
    </section>
  </conbody> 
</concept>
    </xsl:result-document>
  </xsl:for-each>
</xsl:template>
</xsl:stylesheet>
