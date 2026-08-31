<?xml version="1.0"?>

<!-- Identifikasi sebagai lembar gaya -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <!-- Impor templat konversi html yang biasa                 -->
  <xsl:import href="/home/jirka/pretext/xsl/pretext-html.xsl"/>

  <!-- Keluaran dimaksudkan untuk dirender oleh html -->
  <!--<xsl:output method="html" />-->

  <!-- apply-imports juga menerapkan yang asli, apply-templates mengabaikan yang asli-->
  <!-- memerlukan nomor yang ditetapkan langsung pada semuanya, sehingga pretext tidak standar -->
  <xsl:template match="exercise|exercises|example|remark|theorem|lemma|proposition|corollary|principle|axiom|definition|chapter|appendix|section|subsection|subsubsection|figure|table" mode="number">
    <xsl:choose>
      <xsl:when test="@number">
        <xsl:value-of select="@number"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-imports/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="mrow|md" mode="number">
    <xsl:choose>
      <xsl:when test="@eqnumber">
        <xsl:value-of select="@eqnumber"/>
      </xsl:when>
      <xsl:when test="../@eqnumber">
        <xsl:value-of select="../@eqnumber"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-imports/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>


  <!-- Menginginkan label referensi yang ditetapkan langsung, sehingga pretext tidak standar -->
  <xsl:template match="biblio" mode="serial-number">
    <xsl:choose>
      <xsl:when test="@tag">
        <xsl:value-of select="@tag"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-imports/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- memerlukan multline, jadi izinkan lingkungan khusus -->
  <xsl:template match="md" mode="displaymath-alignment">
    <xsl:choose>
      <xsl:when test="@latexenv">
        <xsl:value-of select="@latexenv"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-imports/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- ADUH, ini tampaknya sebuah siasat; ini akan menambahkan atribut start jika diberikan -->
  <xsl:template match="ol" mode="insert-paragraph-id">
    <xsl:apply-imports/>
    <xsl:if test="@start">
      <xsl:attribute name="start">
        <xsl:value-of select="@start"/>
      </xsl:attribute>
    </xsl:if>
  </xsl:template>

  <!-- memerlukan pemisah baris, sehingga pretext tidak standar -->
  <xsl:template match="diffyqsbr">
    <br/>
  </xsl:template>

  <!-- memerlukan hr (sejauh ini hanya digunakan untuk memisahkan gambar), sehingga pretext tidak standar -->
  <xsl:template match="diffyqshr">
    <hr class="diffyqshr"/>
  </xsl:template>

  <!-- memerlukan gambar sebaris, width khusus, maxwidth, dan sebagainya, sehingga tidak standar -->
  <!-- gambar harus tanpa ekstensi; .svg ditambahkan -->
  <xsl:template match="diffyqsimage">
    <xsl:element name="img">
      <xsl:attribute name="class">
        <xsl:text>diffyimg</xsl:text>
        <xsl:if test="@float">
          <xsl:choose>
            <xsl:when test="@float = 'left'">
              <xsl:text> diffyfloatleft</xsl:text>
            </xsl:when>
            <xsl:when test="@float = 'right'">
              <xsl:text> diffyfloatright</xsl:text>
            </xsl:when>
          </xsl:choose>
        </xsl:if>
      </xsl:attribute>
      <xsl:attribute name="style">
        <xsl:if test="@width">
          <xsl:text>width:</xsl:text>
          <xsl:value-of select="@width"/>
          <xsl:text>; </xsl:text>
        </xsl:if>
        <xsl:if test="@maxwidth">
          <xsl:text>max-width:</xsl:text>
          <xsl:value-of select="@maxwidth"/>
          <xsl:text>; </xsl:text>
        </xsl:if>
        <xsl:if test="@height">
          <xsl:text>height:</xsl:text>
          <xsl:value-of select="@height"/>
          <xsl:text>; </xsl:text>
        </xsl:if>
        <xsl:if test="@background-color">
          <xsl:text>background-color:</xsl:text>
          <xsl:value-of select="@background-color"/>
          <xsl:text>; </xsl:text>
        </xsl:if>
		<!--<xsl:text>margin:auto; vertical-align:middle;</xsl:text>-->
        <xsl:choose>
          <xsl:when test="@inline = 'yes'">
				</xsl:when>
          <xsl:otherwise>
            <xsl:text>display:block;</xsl:text>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
      <xsl:attribute name="src">
        <xsl:value-of select="@source"/>
        <xsl:text>.svg</xsl:text>
      </xsl:attribute>
      <!-- Untuk aksesibilitas, gunakan peran ARIA, misalnya agar -->
      <!-- pembaca layar tidak mencoba membaca elemen SVG          -->
      <!-- Catatan: jika kita menulis SVG ke dalam halaman, letakkan -->
      <!-- atribut ini pada elemen "svg"                          -->
      <xsl:attribute name="role">
          <xsl:text>img</xsl:text>
      </xsl:attribute>
      <!-- atribut alt untuk aksesibilitas -->
      <xsl:choose>
          <xsl:when test="@decorative = 'yes'">
              <xsl:attribute name="alt"/>
          </xsl:when>
          <xsl:when test="shortdescription">
              <xsl:attribute name="alt">
                  <xsl:apply-templates select="shortdescription"/>
              </xsl:attribute>
          </xsl:when>
          <xsl:when test="description">
              <xsl:attribute name="alt">
                  <xsl:text>dijelaskan secara terperinci setelah gambar</xsl:text>
              </xsl:attribute>
              <xsl:attribute name="aria-describedby">
                  <xsl:apply-templates select="." mode="describedby-id"/>
              </xsl:attribute>
          </xsl:when>
      </xsl:choose>
    </xsl:element>
  </xsl:template>

  <!-- kita hampir tidak pernah merujuk gambar/tabel dari jauh, sehingga membuat 
       xref menjadi knowl tampaknya tidak perlu dan hanya sedikit membingungkan -->
  <xsl:template match="figure|table" mode="xref-as-knowl">
    <xsl:value-of select="false()" />
  </xsl:template>

  <xsl:param name="debug.datedfiles" select="'no'"/>

  <xsl:param name="html.css.extra" select="'extra.css'"/>

</xsl:stylesheet>


