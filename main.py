import os
import sys

def limpar_tela():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def interpretador_dom():
    arquivo_script = "script.dom"

    
    if not os.path.exists(arquivo_script):
        print(f"❌ ERRO: Arquivo '{arquivo_script}' não encontrado na pasta atual.")
        return

    limpar_tela()
    print("="*50)
    print("☢️  DOMER OS - INTERPRETADOR DE SCRIPT v2.0 ☢️")
    print(f"📂 Rodando: {os.path.abspath(arquivo_script)}")
    print("="*50 + "\n")

    try:
        with open(arquivo_script, "r", encoding="utf-8") as f:
            
            instrucoes = f.readlines()
            
            for num_linha, linha in enumerate(instrucoes, 1):
                linha = linha.strip()
                
                # Pula linhas vazias ou que são apenas comentários
                if not linha or linha.startswith("#"):
                    continue

                # --- COMANDO: falar ---
                if linha.startswith("falar"):
                    if '"' in linha:
                        msg = linha.split('"')[1]
                        print(f"📢 [SAÍDA]: {msg}")
                    else:
                        print(f"⚠️  ERRO (Linha {num_linha}): Use aspas para falar. Ex: falar \"olá\"")

                # --- COMANDO: calcular ---
                elif linha.startswith("calcular"):
                    try:
                        conta = linha.replace("calcular", "").strip()
                        # O eval() processa a matemática básica
                        resultado = eval(conta)
                        print(f"🔢 [CÁLCULO]: {conta} = {resultado}")
                    except Exception as e:
                        print(f"⚠️  ERRO (Linha {num_linha}): Cálculo inválido -> {e}")

                # --- COMANDO NÃO RECONHECIDO ---
                else:
                    print(f"❓ COMANDO DESCONHECIDO (Linha {num_linha}): {linha}")

    except Exception as e:
        print(f"❌ ERRO AO PROCESSAR O ARQUIVO: {e}")

    print("\n" + "="*50)
    print("✅ EXECUÇÃO FINALIZADA")
    print("="*50)

if __name__ == "__main__":
    interpretador_dom()
    
