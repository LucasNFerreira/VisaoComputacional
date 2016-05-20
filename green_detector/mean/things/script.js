//Configuracoes
var dashboard = document.getElementById('grafico_area');
var docHeight = document.documentElement.clientHeight - 20; // - 20 jsFiddle hack
var docWidth = document.documentElement.clientWidth - 20;
dashboard.height = docHeight;
dashboard.width = docWidth;
var ctx;
var _y = docHeight - 20; // jsfiddle hack
// objeto para ser preenchido do tipo Grafico de area
var grafico = {
    espessura: 20,
    cor: '#B1B980',
    dotsColor:'#50545B',
    areaCor:'#FF5B64',
    gap: 5,
    dataProvider: [],
    init: function () {
        var max = this.dataProvider.length;
        ctx = dashboard.getContext('2d');
        ctx.beginPath();
        ctx.moveTo(posicaoX(0), posicaoY(this.dataProvider[0]));
        for (var i = 1; i < max; i++) {
          ctx.lineTo(posicaoX(i), posicaoY(this.dataProvider[i]));            
        }
        // para o chart de area
         ctx.lineTo(posicaoX(max-1),posicaoX(max));
         ctx.lineTo(0,docHeight);
         ctx.strokeStyle = this.cor;
         ctx.lineWidth = this.espessura*0.3;
         ctx.fillStyle=this.areaCor;
         ctx.fill();
         ctx.stroke(); 
         ctx.closePath();
        
        for (var i = 0; i < max; i++)
        {
            ctx.beginPath();
            ctx.arc(posicaoX(i), posicaoY(this.dataProvider[i]), this.espessura * 0.5, 0, Math.PI * 2, false);
            ctx.fillStyle= this.dotsColor;
            ctx.fill();
            ctx.closePath();
        }       
    }
}

function pegarValorMaximo() {
    var max = 0;
    for (var i = 0; i < grafico.dataProvider.length; i++) {
         if (grafico.dataProvider[i] > max) {
             max = grafico.dataProvider[i];
         }
    }
    max += 10 - max % 10;
    return max;
}

function posicaoY(val) {
   return docHeight - ((docHeight-20) / pegarValorMaximo()) * val;
}
function posicaoX(val) {
    return (docWidth / grafico.dataProvider.length) * val;
}
// usando um provedor de dados para preencher
grafico.cor = "#75bc48";
grafico.dataProvider = [2.35938, 3.09375, 2.20703, 7.19141, 8.97266, 5.83984, 4.375, 2.80859, 2.99609, 8.16797, 2.04297, 0.253906, 14.375, 8.89844, 
                        5.77734, 6.34375, 7.11328, 7.80078, 13.4023, 33.6602, 38.2578, 42.3945, 42.75, 39.4102, 39.7383, 35.7656, 43.4531, 51.8711,
                        59.75, 63.7383, 60.4688, 56.4922, 51.8008, 54.3789, 53.3594, 53.1797, 54.1602, 51.2969, 48.6797, 50.4141, 56.7422, 52.3008, 
                        54.7656, 62.0, 70.543, 71.8828, 75.7695, 75.1797, 79.8047, 75.3086, 66.6523, 28.3555, 15.707, 14.4023, 10.3867, 10.5547, 
                        10.0625, 37.1133, 68.2773, 82.1406, 79.1328, 71.1602, 67.4844, 66.3242, 52.1602, 53.5469, 50.25, 42.3438, 45.4375, 50.75,
                        58.8008, 58.6328, 72.1641, 83.1758, 81.8711, 52.5352, 7.35938, 2.80078, 0.00390625, 0.0078125, 0.222656, 0.617188, 0.425781,
                        0.625, 0.414062 ];
grafico.columnHeight = 20; // seta largura da coluna
grafico.init(); // inicializa