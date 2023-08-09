# Define UI for app that draws a histogram ----
library(shiny)

# Define UI for app that draws a histogram ----
ui <- fluidPage(
  
  tags$head(
    tags$style(
      HTML("body {background-color: #dcdcdc;}")
    )
  ),
  # App title ----
  titlePanel("Histograma x Boxplot"),

  # Sidebar layout with input and output definitions ----
  sidebarLayout(
    position = 'left',
    
    # Sidebar panel for inputs ----
    sidebarPanel(
      radioButtons("dist", "Tipo de Distribuiução:",
                   c("Simétrica" = "runif",
                     "Assimétrica" = "rgamma"
                   )),

      # Input: Slider for the number of bins ----
      sliderInput(inputId = "bins",
                  label = "Amostra",
                  min = 1,
                  max = 50,
                  value = 10)
      
    ),
    # Main panel for displaying outputs ----
    mainPanel(
      # Output: Histogram ----
      plotOutput(outputId = "distPlot", height = 600, width = 900)
      
    )
  )
)
# Define server logic required to draw a histogram ----
server <- function(input, output) {
  output$distPlot <- renderPlot({
    dist <- switch(input$dist,
                   runif = 1,
                   rgamma = 2)
    if(dist==1){
      n = 100
      x2    <- runif(n, min = -5, max = 5)
      bins <- seq(min(x2), max(x2), length.out = input$bins + 10)
      par(mfrow=c(2,1))
      layout(matrix(c(1,1,1,2,2,2), byrow = TRUE))
      hist(x=x2, breaks = 'sturges', main='Histogram', cex.main=2, col='navajowhite')
      boxplot(x=x2, main="Boxplot", horizontal=TRUE, axes=FALSE, cex.main=2, col='navajowhite')
      axis(2)
      axis(1)
    }
    
    if(dist==2){
      n = 100
      x3    <- rgamma(n,10, rate = 0.5)
      bins <- seq(min(x3), max(x3), length.out = input$bins + 10)
      par(mfrow=c(2,1))
      layout(matrix(c(1,1,1,2,2,2), byrow = TRUE))
      hist(x=x3, breaks = 'sturges', main='Histogram', cex.main=2, col='navajowhite')
      boxplot(x=x3, main="Boxplot", horizontal=TRUE, axes=FALSE,  cex.main=2, col='navajowhite')
      box(bty="l")
      axis(2)
      axis(1)
    }
  })
}

shinyApp(ui, server)



















