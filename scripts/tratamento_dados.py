import pandas as pd

def processar_csv(caminho_entrada, caminho_saida, nomes_colunas):  
    df = pd.read_csv(caminho_entrada,  
                    skiprows=2, 
                    sep=";", 
                    skipfooter=24,
                    na_values="-",
                    engine='python'
                    )
    
    df.columns = nomes_colunas
    
    df_preenchido = df.fillna(0)

    df_preenchido.to_csv(caminho_saida, 
                        index=False, 
                        sep=";",
                        encoding="latin1"
                        )

processar_csv(r"C:\Users\Gustavo\Documents\Projetos\area_vs_rendimento\dados\brutos\area_plantada.csv",
              r"C:\Users\Gustavo\Documents\Projetos\area_vs_rendimento\dados\tratados\area_tratado.csv",
              ["UF", "Cultura", "Ano", "Area Plantada (ha)"]
              )

processar_csv(r"C:\Users\Gustavo\Documents\Projetos\area_vs_rendimento\dados\brutos\rendimento.csv",
              r"C:\Users\Gustavo\Documents\Projetos\area_vs_rendimento\dados\tratados\rendimento_tratado.csv",
              ["UF", "Cultura", "Ano", "Rendimento (kg/ha)"]
              )


