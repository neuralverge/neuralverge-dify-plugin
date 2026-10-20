# NeuralVerge for Dify

NeuralVerge is the data layer for agentic AI.

Ask a question in plain language and get a structured, cited answer drawn from 300+ sources — e-commerce marketplaces, corporate registries, company intelligence, enrichment and social — plus the open web. Connect over MCP or REST.

**What's inside**

- **E-commerce & marketplaces** — 128 sources: Amazon, eBay, Walmart, AliExpress, Alibaba, Shopify, Target, Zalando, Rakuten, Flipkart and more
- **Corporate registries** — 95: UK, France, Spain, the Netherlands, Sweden, Norway, Poland, Brazil, Canada, Australia and more
- **Startup & funding data** — 93: Dealroom, PitchBook, Tracxn, Owler, Product Hunt, Y Combinator, Wellfound, Kickstarter, Indiegogo, Seedrs and more
- **Company intelligence** — 16: Crunchbase, Gartner Peer Insights, Capterra, Trustpilot
- **B2B data** — 7: Company and people search, Company and people profiles, Company employees
- **Enrichment:** Email lookup, Phone lookup, LinkedIn Finder, Email finder

Teams use NeuralVerge for agentic products, go-to-market, outbound, market research, competitor analysis, brand monitoring, public procurement, e-commerce intelligence, due diligence, KYC/KYB and recruiting. Works with Claude, ChatGPT, Gemini, Cursor and any MCP client.

→ [neuralverge.ai](https://neuralverge.ai)

## About this plugin

This plugin exposes the [NeuralVerge](https://neuralverge.ai) API as 342 Dify tools:

- **Run Web Search** (`run_search`) — ranked web results in one synchronous call.
- **Run AI Extract** (`run_extract`) — load a page by URL and extract structured data from natural-language instructions and/or a JSON schema.
- **Data Sources** — company registries, marketplaces, product reviews, LinkedIn, email and phone enrichment, Crunchbase and more. One tool per endpoint, for example `run_cz_companies_search` or `run_amazon_product`.

Every tool is a thin wrapper over one endpoint of the [NeuralVerge REST API](https://docs.neuralverge.ai); the tool descriptions state what each call returns and what it costs in points.

## Setup

1. Create an API key in the NeuralVerge dashboard under **Settings → API**.
2. In Dify, open **Plugins → NeuralVerge → Authorize** and paste the key.
3. Add the tools you need to an Agent or Workflow. With 342 tools, enable only the ones the task requires: every enabled tool's definition costs model context.

## Parameters

- Array parameters are entered as a comma-separated list.
- Nested `settings` objects are flattened: `settings.country` becomes `settings_country`.
- Results are returned as JSON, exactly as the API returns them.

## Network and data

The plugin only calls `https://api.neuralverge.ai`. See [PRIVACY.md](PRIVACY.md).

## Also available as an MCP server

The same tools are available over the Model Context Protocol: [MCP Server docs](https://docs.neuralverge.ai/mcp-server).

## Source

Source: https://github.com/neuralverge/neuralverge-dify-plugin. The tool definitions under `tools/` are generated from the NeuralVerge MCP server's tool catalog, which is why they are uniform.
