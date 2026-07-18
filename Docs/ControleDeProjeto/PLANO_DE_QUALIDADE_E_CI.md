# Plano de Qualidade e CI

- Projeto: Nat 1 RPG Engine
- Versão: 1.0
- Data: 2026-07-18
- Status: baseline preparada no working tree; CI remoto depende de integração

## Objetivo

Transformar validações locais em gates reproduzíveis para cada Pull Request, cobrindo
código, banco, migrations, segurança de dependências e build entregável.

## Pipeline obrigatório

O workflow canônico fica em `.github/workflows/ci.yml` e usa permissões somente de
leitura para o conteúdo do repositório.

### Job backend

1. iniciar PostgreSQL 16 efêmero com healthcheck;
2. instalar `requirements.lock` em Python 3.12;
3. executar `pip check`;
4. executar Ruff;
5. executar testes unitários rápidos;
6. aplicar `alembic upgrade head`;
7. executar `alembic current` e `alembic check`;
8. executar teste integrado real sem `Base.metadata.create_all()`;
9. provar reversibilidade com `downgrade base → upgrade head` no banco efêmero;
10. auditar dependências Python.

### Job frontend

1. instalar o lock com `npm ci` em Node 22;
2. executar ESLint com zero warnings;
3. executar TypeScript;
4. executar Vitest;
5. gerar build Vite;
6. executar auditoria npm com bloqueio em severidade alta.

## Pirâmide de testes

| Camada | Objetivo | Frequência |
| --- | --- | --- |
| Unitário | regras puras, schemas, apresentação e helpers | todo PR |
| Service/repository | transições, isolamento e erros de domínio | todo PR |
| PostgreSQL integrado | migration, tipos, constraints e CRUD real | todo PR |
| Componente | formulário, acessibilidade e estados assíncronos | todo PR com UI |
| Contrato/API | payloads e códigos estáveis entre frontend/backend | vertical funcional |
| E2E | cadastro → campanha → sessão → recap | antes do piloto e release |
| Segurança | IDOR, auth, configuração e dependências | todo PR + revisão por fase |
| Visual | regressão de telas e breakpoints críticos | antes do piloto e mudanças de marca |

SQLite em memória permanece útil para feedback rápido, mas não substitui migrations ou
PostgreSQL no gate.

## Política de migrations

- model novo exige revision Alembic revisada;
- CI deve falhar se `alembic check` detectar drift;
- rollback completo só é testado em banco descartável;
- banco local persistente nunca recebe `downgrade base` como validação automática;
- produção executa migration uma vez por release, com backup e plano de compatibilidade;
- mudanças destrutivas usam estratégia expand/contract quando houver dados reais.

## Dependências e supply chain

- dependências diretas Python possuem versão fixa;
- `requirements.lock` registra o ambiente reproduzível de CI/desenvolvimento;
- `package-lock.json` é obrigatório e CI usa `npm ci`;
- atualizações são Pull Requests intencionais, com changelog, auditoria e testes;
- vulnerabilidade não autoriza atualização cega nem exceção silenciosa;
- exceção temporária exige risco, versão afetada, mitigação, responsável e prazo;
- auditorias online compartilham metadados de dependências com seus serviços; sua
  execução deve ocorrer no ambiente CI autorizado ou com aprovação explícita local.

## Gates por tipo de mudança

| Mudança | Gates mínimos |
| --- | --- |
| Documentação | links, coerência, espaços, `git diff --check` |
| Backend sem banco | Ruff, unitários, `pip check`, auditoria |
| Model/migration | backend completo, PostgreSQL e ciclo reversível |
| Frontend | lint, typecheck, testes, build, auditoria e QA responsivo |
| Auth/autorização | backend completo, IDOR, configuração, threat model |
| Vertical full stack | todos os jobs, contrato, E2E e smoke manual |
| Release | CI verde, migrations, backup/restore, observabilidade e checklist de deploy |

## Estados obrigatórios de UI

Toda tela conectada deve possuir:

- loading sem layout enganoso;
- erro com próximo passo e retry quando seguro;
- vazio que explica como obter valor;
- sucesso confirmado sem depender apenas de cor;
- estado desabilitado justificado;
- prevenção de duplo envio;
- perda de conexão e recuperação para editores críticos.

## Acessibilidade e QA visual

Checklist mínimo:

- HTML semântico e hierarquia de headings;
- label, nome e autocomplete em controles;
- foco visível e ordem de teclado;
- dialogs com foco inicial, Escape, retorno de foco e scroll contido;
- `aria-live` para alterações assíncronas relevantes;
- contraste WCAG AA nos pares efetivamente usados;
- alvos de toque adequados;
- `prefers-reduced-motion`;
- imagens com dimensões, texto alternativo e carregamento apropriado;
- breakpoints móvel, tablet, desktop e zoom de 200%;
- conteúdo curto, médio, longo e caracteres internacionais.

## Observabilidade de qualidade

Antes do beta, medir:

- taxa de erro por endpoint e fluxo;
- duração p50/p95;
- falhas de login e rate limiting sem e-mail em log aberto;
- falha e duração de migration;
- erros de frontend por versão;
- sucesso do fluxo sessão/recap;
- regressões de acessibilidade e build.

Logs devem usar request/correlation ID e códigos de erro, sem token, senha, e-mail aberto
ou conteúdo narrativo.

## Critério de integração

Uma branch está pronta para PR quando:

- escopo e diff foram revisados;
- CI equivalente foi executado localmente quando possível;
- PostgreSQL real foi usado quando aplicável;
- documentação registra resultados verdadeiros;
- não há secret ou artefato local;
- `git diff --check` está limpo;
- pendências e warnings possuem decisão explícita;
- Gabriel aprovou commit e integração conforme o protocolo.
