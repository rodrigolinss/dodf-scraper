# Projeto de Busca de Termo no Diário Oficial do DF

Este projeto tem como objetivo automatizar a busca diária de documentos no Diário Oficial do Distrito Federal (DODF). O código é executado periodicamente para localizar as páginas mais recentes que contenham o PDF intitulado "INTEGRA.pdf" e verificar se elas contêm o termo pesquisado (por exemplo, "ibanes"). A ideia é fornecer uma maneira prática de monitorar o DODF em busca de informações relevantes de forma automatizada.

## Objetivo

A intenção é que este projeto seja executado diariamente para verificar as publicações mais recentes do DODF e procurar por um termo específico. Quando o PDF for encontrado, o código verifica se o termo está presente nas páginas do documento.

### Funcionalidade Esperada
- **Busca diária no DODF**: O script será executado todos os dias para procurar por documentos atualizados contendo o PDF "INTEGRA.pdf".
- **Verificação de termo no conteúdo do PDF**: O termo de busca será especificado no código (como "ibanes"), e o script irá verificar se esse termo está presente no conteúdo extraído do PDF.
- **Relatório diário**: O script retorna as páginas do DODF que contêm o PDF e, caso o termo esteja presente, uma indicação será fornecida.

## Como Funciona

O script acessa o Diário Oficial do DF, localiza o link do PDF intitulado "INTEGRA.pdf", baixa o documento, e procura por um termo específico dentro do conteúdo do PDF. Se o termo for encontrado, uma mensagem é exibida indicando o sucesso da busca.

## Status Atual

Este projeto está **em fase de teste**. O objetivo principal neste momento é validar a busca diária de PDFs no DODF e a extração de informações a partir do conteúdo desses documentos. O código ainda está sendo ajustado e pode não estar completamente funcional em todos os cenários.

### Pontos em Teste:
- **Busca no Diário Oficial**: Garantir que o link para o PDF "INTEGRA.pdf" seja localizado corretamente.
- **Extração de conteúdo do PDF**: Verificar se o conteúdo do PDF está sendo extraído corretamente para buscar o termo.
- **Execução Diária**: Estabelecer a automação diária para garantir que o código execute a busca e retorne as informações corretamente.
