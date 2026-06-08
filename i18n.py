from typing import Dict

LANGUAGE_OPTIONS = {
    "English": "en",
    "German (Deutsch)": "de",
    "Persian (فارسی)": "fa",
}


TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "en": {
        # Hero / landing
        "hero_title_line_1": "Sovereign Evidence.",
        "hero_title_highlight": "Scientifically Traceable.",
        "hero_subtitle": (
            "A Dockerized research decision support system for scientific claim triage, "
            "evidence discovery, and transparent academic data lineage."
        ),
        # Auth
        "auth_header_title": "Access Gatekeeper",
        "auth_header_subtitle": "Authenticate to access the verification engine.",
        "auth_missing_credentials": "Access denied: missing credentials. Please provide both email and token.",
        "auth_verifying": "Cryptographically verifying credentials...",
        "auth_success": "Authentication successful. Initializing workspace...",
        "auth_form_title": "Researcher Login",
        "auth_email_label": "Institutional Email",
        "auth_email_placeholder": "researcher@university.edu",
        "auth_password_label": "Access Token / Password",
        "auth_tier_label": "Select Mock Tier (For Demo)",
        "auth_submit": "Authenticate & Initialize",
        # Sidebar groups
        "group_verification_workflow": "Verification Workflow",
        "group_research_governance": "Research Governance",
        "group_display": "Display",
        "display_matrix": "Display Matrix",
        "system_language": "System Language",
        "commercial_disabled_caption": "Commercial modules are disabled in the academic demo build.",

        # Navigation
        "nav_research_engine": "Research Engine",
        "nav_system_telemetry": "System Telemetry",
        "nav_methods": "Methods & Limitations",
        "nav_deep_audit": "Deep Audit",
        "nav_data_lineage_vault": "Data Lineage Vault",

        # Status
        "status_infrastructure": "Infrastructure",
        "status_online": "Online",
        "status_mode": "Mode",
        "status_academic_dss": "Academic DSS",
        "status_model": "MODEL",

        # Research page
        "research_title": "VeriClaim Research Engine",
        "research_subtitle": "Evidence discovery and claim triage for open-science research workflows.",
        "scientific_claim": "Scientific claim",
        "claim_placeholder": "e.g., Microplastics are detectable in human blood",
        "initiate_verification": "Initiate Verification",
        "active_workspace": "Active Investigation Workspace",
        "refine_query": "Refine Query",
        "reevaluate": "Re-Evaluate",
        "reset_workspace": "Reset Workspace",

        # Pipeline messages
        "no_local_evidence": "No local evidence found for '{query}'. Launching n8n + OpenAlex pipeline...",
        "pipeline_progress": "OpenAlex retrieval and LLM-based claim triage in progress...",
        "pipeline_completed": "Pipeline completed. Refreshing the research data store...",
        "pipeline_failed": "Pipeline failed. Check n8n executions and Postgres credentials.",
        "no_vectors_persisted": "No evidence vectors were persisted for this query yet.",
        "gateway_fault": "Gateway fault: cannot reach the n8n orchestrator.",
        "pipeline_timeout": "Pipeline timeout: the n8n inference graph exceeded the configured limit.",

        # Analytics
        "epistemic_overview": "Epistemic Consensus Overview",
        "mean_reliability": "Mean Reliability Index",
        "evidence_vectors": "Evidence Vectors",
        "mean_certainty": "Mean Certainty",
        "aggregated_citations": "Aggregated Citations",
        "found_vectors": "Found {count} scored evidence vectors.",

        # Cards
        "supported": "Supported",
        "mixed": "Mixed / Debatable",
        "refuted": "Refuted",
        "insufficient_evidence": "Insufficient Evidence",
        "citations": "Citations",
        "year": "Year",
        "extracted_claim": "Extracted claim",
        "model_rationale": "Model rationale",
        "reliability_index": "Reliability Index",
        "source": "Source",

        # Dashboard
        "dashboard_title": "System Telemetry & Epistemic Insights",
        "dashboard_subtitle": "Operational overview for the VeriClaim research data store",
        "no_dashboard_data": "No telemetry data is available yet. Run a claim verification first.",
        "evidence_vectors": "Evidence Vectors",
        "mean_reliability": "Mean Reliability Index",
        "open_access": "Open Access",
        "total_citations": "Total Citations",
        "verdict_distribution": "Verdict Distribution",
        "domain_distribution": "Scientific Domain Distribution",
        "recent_vectors": "Recent Evidence Vectors",
        "verified_at": "Verified at",
        "verdict": "Verdict",
        "reliability_index": "Reliability Index",
        "domain": "Domain",
        "title": "Title",
        "claim": "Claim",

        # Vault
        "vault_title": "Data Lineage Vault",
        "vault_subtitle": "Auditable storage layer for claims, verdicts, and evidence references",
        "filter_vault": "Filter vault",
        "filter_placeholder": "Filter by title, claim, verdict, domain...",
        "export_csv": "Export filtered vault as CSV",
        "no_vault_data": "No lineage records are available yet.",
        "title": "Title",
        "claim": "Claim",
        "verdict": "Verdict",
        "domain": "Domain",
        "verified_at": "Verified at",
        "publication_year": "Publication Year",

        # Deep Audit
        "deep_audit_title": "Deep Audit",
        "deep_audit_subtitle": "Batch verification concept for PDF and CSV inputs",
        "deep_audit_stub": "This module is intentionally kept as a research-roadmap stub in the academic demo build.",
        "planned_workflow": "Planned workflow:",
        "deep_audit_step_1": "The researcher uploads a PDF or CSV file.",
        "deep_audit_step_2": "Streamlit forwards the file to a dedicated n8n webhook.",
        "deep_audit_step_3": "n8n extracts candidate scientific claims and stores them in PostgreSQL.",
        "deep_audit_step_4": "The verification pipeline processes extracted claims asynchronously.",
        "deep_audit_step_5": "The Data Lineage Vault displays auditable outputs, evidence references, and processing metadata.",
        "deep_audit_mvp_note": "The current single-claim engine is the stable MVP path. Batch processing is intentionally postponed until the OpenAlex workflow, database schema, and evidence cards are fully stable.",
        "upload_future": "Upload PDF or CSV for future batch-audit workflow",
        "batch_disabled": "Batch upload is disabled in this funding-demo build and documented as a next milestone.",
       
       # Methods page extended
        "methods_positioning_body": "VeriClaim is a research decision support system for scientific claim triage. It does not claim to replace peer review, systematic review, domain experts, or clinical/scientific judgment.",
        "methods_pipeline_intro": "The current academic prototype follows a four-stage pipeline:",
        "methods_claim_intake_title": "Claim intake",
        "methods_claim_intake_body": "A user submits a scientific claim or research question.",
        "methods_query_compression_title": "Query compression",
        "methods_query_compression_body": "An LLM converts the input into a concise OpenAlex-oriented search phrase.",
        "methods_evidence_retrieval_title": "Evidence retrieval",
        "methods_evidence_retrieval_body": "OpenAlex metadata, abstracts, citation counts, DOI links, and topical metadata are retrieved.",
        "methods_evidence_scoring_title": "Evidence scoring",
        "methods_evidence_scoring_body": "An LLM extracts a core claim and assigns a preliminary verdict and confidence score.",
        "methods_reliability_body": "The reliability score is a heuristic research signal, not a truth certificate. In the current demo build, it combines citation velocity, linguistic certainty, open-access transparency, and publication recency.",
        "methods_supported_definition": "the evidence vector appears to support the extracted claim.",
        "methods_mixed_definition": "the evidence vector is preliminary, ambiguous, or partially conflicting.",
        "methods_refuted_definition": "the evidence vector appears to contradict the extracted claim.",
        "methods_insufficient_definition": "the abstract or metadata is too weak for a meaningful assessment.",
        "methods_limitation_abstract": "Abstract-level analysis can miss important methodological details from the full paper.",
        "methods_limitation_citations": "Citation count is not equivalent to scientific validity.",
        "methods_limitation_llm": "LLM-generated verdicts may be sensitive to prompt wording and metadata quality.",
        "methods_limitation_sources": "The current prototype uses OpenAlex only; Semantic Scholar, PubMed, arXiv, and Europe PMC are future extensions.",
        "methods_limitation_consensus": "Contradictory literature is not yet modeled as a full cross-paper consensus graph.",
        "methods_intended_use_body": "The system is intended for early-stage research discovery, evidence mapping, demonstrable research data management, and reproducible open-science prototyping.",
        "methods_demo_framing": "Recommended demo framing: evidence discovery and claim triage, not automated scientific truth.",

        # Academic positioning
        "not_peer_review": "This system is not a replacement for peer review or domain expertise.",
        "evidence_level_note": "Verdicts are evidence-level signals, not final claim-level truth decisions.",
        "future_consensus_layer": "A cross-paper consensus layer is planned as a future research milestone.",
    },

    "de": {
        # Hero / landing
        "hero_title_line_1": "Souveräne Evidenz.",
        "hero_title_highlight": "Wissenschaftlich nachvollziehbar.",
        "hero_subtitle": (
            "Ein Docker-basiertes Forschungs-DSS für wissenschaftliche Claim-Triage, "
            "Evidenzsuche und transparente akademische Datenherkunft."
        ),
        # Auth
        "auth_header_title": "Zugangskontrolle",
        "auth_header_subtitle": "Authentifizieren Sie sich, um auf die Verifikations-Engine zuzugreifen.",
        "auth_missing_credentials": "Zugriff verweigert: Zugangsdaten fehlen. Bitte E-Mail und Token angeben.",
        "auth_verifying": "Zugangsdaten werden kryptografisch geprüft...",
        "auth_success": "Authentifizierung erfolgreich. Arbeitsbereich wird initialisiert...",
        "auth_form_title": "Forscher-Login",
        "auth_email_label": "Institutionelle E-Mail",
        "auth_email_placeholder": "researcher@university.edu",
        "auth_password_label": "Zugangs-Token / Passwort",
        "auth_tier_label": "Mock-Stufe auswählen (für Demo)",
        "auth_submit": "Authentifizieren & initialisieren",
        # Sidebar groups
        "group_verification_workflow": "Verifikations-Workflow",
        "group_research_governance": "Forschungsgovernance",
        "group_display": "Anzeige",
        "display_matrix": "Darstellungsmodus",
        "system_language": "Systemsprache",
        "commercial_disabled_caption": "Kommerzielle Module sind in dieser akademischen Demo deaktiviert.",

        # Navigation
        "nav_research_engine": "Recherche-Engine",
        "nav_system_telemetry": "Systemtelemetrie",
        "nav_methods": "Methoden & Grenzen",
        "nav_deep_audit": "Deep Audit",
        "nav_data_lineage_vault": "Data-Lineage-Tresor",

        # Status
        "status_infrastructure": "Infrastruktur",
        "status_online": "Online",
        "status_mode": "Modus",
        "status_academic_dss": "Akademisches DSS",
        "status_model": "MODELL",

        # Research page
        "research_title": "VeriClaim Recherche-Engine",
        "research_subtitle": "Evidenzsuche und Claim-Triage für Open-Science-Forschungsworkflows.",
        "scientific_claim": "Wissenschaftliche Aussage",
        "claim_placeholder": "z. B. Microplastics are detectable in human blood",
        "initiate_verification": "Verifikation starten",
        "active_workspace": "Aktiver Untersuchungsbereich",
        "refine_query": "Abfrage verfeinern",
        "reevaluate": "Neu bewerten",
        "reset_workspace": "Arbeitsbereich zurücksetzen",

        # Pipeline messages
        "no_local_evidence": "Keine lokale Evidenz für '{query}' gefunden. n8n + OpenAlex-Pipeline wird gestartet...",
        "pipeline_progress": "OpenAlex-Abruf und LLM-basierte Claim-Triage laufen...",
        "pipeline_completed": "Pipeline abgeschlossen. Forschungsdatenspeicher wird aktualisiert...",
        "pipeline_failed": "Pipeline fehlgeschlagen. Bitte n8n-Ausführungen und Postgres-Zugangsdaten prüfen.",
        "no_vectors_persisted": "Für diese Anfrage wurden noch keine Evidenzvektoren gespeichert.",
        "gateway_fault": "Gateway-Fehler: Der n8n-Orchestrator ist nicht erreichbar.",
        "pipeline_timeout": "Pipeline-Timeout: Der n8n-Inferenzgraph hat das konfigurierte Limit überschritten.",

        # Analytics
        "epistemic_overview": "Epistemische Konsensübersicht",
        "mean_reliability": "Mittlerer Reliability Index",
        "evidence_vectors": "Evidenzvektoren",
        "mean_certainty": "Mittlere Sicherheit",
        "aggregated_citations": "Aggregierte Zitationen",
        "found_vectors": "{count} bewertete Evidenzvektoren gefunden.",

        # Cards
        "supported": "Unterstützt",
        "mixed": "Gemischt / strittig",
        "refuted": "Widerlegt",
        "insufficient_evidence": "Unzureichende Evidenz",
        "citations": "Zitationen",
        "year": "Jahr",
        "extracted_claim": "Extrahierte Aussage",
        "model_rationale": "Modellbegründung",
        "reliability_index": "Reliability Index",
        "source": "Quelle",

        # Dashboard
        "dashboard_title": "Systemtelemetrie & epistemische Einblicke",
        "dashboard_subtitle": "Operativer Überblick über den VeriClaim-Forschungsdatenspeicher",
        "total_articles": "Artikel gesamt",
        "total_claims": "Claims gesamt",
        "total_verifications": "Verifikationen gesamt",
        "open_access": "Open Access",
        "total_citations": "Zitationen gesamt",
        "verdict_distribution": "Verteilung der Bewertungen",
        "domain_distribution": "Verteilung wissenschaftlicher Domänen",
        "recent_vectors": "Aktuelle Evidenzvektoren",
        "no_dashboard_data": "Noch keine Telemetriedaten verfügbar. Bitte zuerst eine Claim-Verifikation ausführen.",

        # Vault
        "vault_title": "Data-Lineage-Tresor",
        "vault_subtitle": "Auditierbare Speicherschicht für Claims, Bewertungen und Evidenzreferenzen",
        "filter_vault": "Tresor filtern",
        "filter_placeholder": "Nach Titel, Claim, Bewertung oder Domäne filtern...",
        "export_csv": "Gefilterten Tresor als CSV exportieren",
        "no_vault_data": "Noch keine Lineage-Datensätze verfügbar.",
        "title": "Titel",
        "claim": "Claim",
        "verdict": "Bewertung",
        "domain": "Domäne",
        "verified_at": "Verifiziert am",
        "publication_year": "Publikationsjahr",

        # Deep Audit
        "deep_audit_title": "Deep Audit",
        "deep_audit_subtitle": "Konzept für Batch-Verifikation von PDF- und CSV-Eingaben",
        "deep_audit_stub": "Dieses Modul bleibt in der akademischen Demo bewusst als Forschungs-Roadmap-Stufe erhalten.",
        "planned_workflow": "Geplanter Workflow:",
        "deep_audit_step_1": "Die Forscherin oder der Forscher lädt eine PDF- oder CSV-Datei hoch.",
        "deep_audit_step_2": "Streamlit leitet die Datei an einen dedizierten n8n-Webhook weiter.",
        "deep_audit_step_3": "n8n extrahiert wissenschaftliche Claim-Kandidaten und speichert sie in PostgreSQL.",
        "deep_audit_step_4": "Die Verifikations-Pipeline verarbeitet die extrahierten Claims asynchron.",
        "deep_audit_step_5": "Der Data-Lineage-Tresor zeigt auditierbare Ergebnisse, Evidenzreferenzen und Verarbeitungsmetadaten.",
        "deep_audit_mvp_note": "Die aktuelle Single-Claim-Engine ist der stabile MVP-Pfad. Batch-Verarbeitung wird bewusst verschoben, bis OpenAlex-Workflow, Datenbankschema und Evidenzkarten vollständig stabil sind.",
        "upload_future": "PDF oder CSV für zukünftigen Batch-Audit-Workflow hochladen",
        "batch_disabled": "Batch-Upload ist in dieser Funding-Demo deaktiviert und als nächster Meilenstein dokumentiert.",
        # Methods page extended
        "methods_positioning_body": "VeriClaim ist ein Forschungs-DSS zur Triage wissenschaftlicher Aussagen. Es ersetzt weder Peer Review, systematische Reviews, Fachexpertise noch klinische oder wissenschaftliche Urteilsbildung.",
        "methods_pipeline_intro": "Der aktuelle akademische Prototyp folgt einer vierstufigen Pipeline:",
        "methods_claim_intake_title": "Claim-Erfassung",
        "methods_claim_intake_body": "Eine Nutzerin oder ein Nutzer gibt eine wissenschaftliche Aussage oder Forschungsfrage ein.",
        "methods_query_compression_title": "Query-Kompression",
        "methods_query_compression_body": "Ein LLM wandelt die Eingabe in eine kurze, auf OpenAlex ausgerichtete Suchphrase um.",
        "methods_evidence_retrieval_title": "Evidenzabruf",
        "methods_evidence_retrieval_body": "OpenAlex-Metadaten, Abstracts, Zitationszahlen, DOI-Links und thematische Metadaten werden abgerufen.",
        "methods_evidence_scoring_title": "Evidenzbewertung",
        "methods_evidence_scoring_body": "Ein LLM extrahiert einen Kern-Claim und weist eine vorläufige Bewertung sowie einen Konfidenzwert zu.",
        "methods_reliability_body": "Der Reliability Score ist ein heuristisches Forschungssignal, kein Wahrheitszertifikat. In der aktuellen Demo kombiniert er Zitationsgeschwindigkeit, sprachliche Sicherheit, Open-Access-Transparenz und Publikationsaktualität.",
        "methods_supported_definition": "der Evidenzvektor scheint den extrahierten Claim zu unterstützen.",
        "methods_mixed_definition": "der Evidenzvektor ist vorläufig, mehrdeutig oder teilweise widersprüchlich.",
        "methods_refuted_definition": "der Evidenzvektor scheint dem extrahierten Claim zu widersprechen.",
        "methods_insufficient_definition": "Abstract oder Metadaten sind zu schwach für eine sinnvolle Bewertung.",
        "methods_limitation_abstract": "Eine Analyse auf Abstract-Ebene kann wichtige methodische Details aus dem Volltext übersehen.",
        "methods_limitation_citations": "Zitationszahlen sind nicht gleichbedeutend mit wissenschaftlicher Validität.",
        "methods_limitation_llm": "LLM-generierte Bewertungen können empfindlich auf Prompt-Formulierungen und Metadatenqualität reagieren.",
        "methods_limitation_sources": "Der aktuelle Prototyp nutzt nur OpenAlex; Semantic Scholar, PubMed, arXiv und Europe PMC sind zukünftige Erweiterungen.",
        "methods_limitation_consensus": "Widersprüchliche Literatur wird noch nicht als vollständiger artikelübergreifender Konsensgraph modelliert.",
        "methods_intended_use_body": "Das System ist für frühe Forschungsrecherche, Evidenzkartierung, demonstrierbares Forschungsdatenmanagement und reproduzierbares Open-Science-Prototyping vorgesehen.",
        "methods_demo_framing": "Empfohlenes Demo-Framing: Evidenzsuche und Claim-Triage, nicht automatisierte wissenschaftliche Wahrheit.",
        # Academic positioning
        "not_peer_review": "Dieses System ersetzt weder Peer Review noch fachliche Expertise.",
        "evidence_level_note": "Bewertungen sind evidenzbezogene Signale, keine endgültigen Wahrheitsentscheidungen auf Claim-Ebene.",
        "future_consensus_layer": "Eine artikelübergreifende Konsensschicht ist als zukünftiger Forschungsmeilenstein geplant.",
    },

    "fa": {
        # Hero / landing
        "hero_title_line_1": "شواهد مستقل.",
        "hero_title_highlight": "قابل ردیابی به‌صورت علمی.",
        "hero_subtitle": (
            "یک سامانه پشتیبان تصمیم پژوهشی مبتنی بر Docker برای اولویت‌بندی ادعاهای علمی، "
            "کشف شواهد و ثبت شفاف ردپای داده‌های آکادمیک."
        ),
        # Auth
        "deep_audit_step_1": "پژوهشگر یک فایل PDF یا CSV آپلود می‌کند.",
        "deep_audit_step_2": "Streamlit فایل را به یک webhook در n8n ارسال می‌کند.",
        "deep_audit_step_3": "n8n ادعاهای احتمالی را استخراج کرده و در PostgreSQL ذخیره می‌کند.",
        "deep_audit_step_4": "Pipeline اعتبارسنجی، ادعاها را به‌صورت غیرهمزمان پردازش می‌کند.",
        "deep_audit_step_5": "مخزن ردپای داده، خروجی‌های قابل ممیزی را نمایش می‌دهد.",
        "deep_audit_mvp_note": "موتور فعلی تک‌ادعایی، مسیر پایدار MVP است. پردازش دسته‌ای باید پس از تثبیت workflow مربوط به OpenAlex، schema و کارت‌های شواهد اضافه شود.",
        # Sidebar groups
        "group_verification_workflow": "جریان اعتبارسنجی",
        "group_research_governance": "حاکمیت پژوهشی",
        "group_display": "نمایش",
        "display_matrix": "حالت نمایش",
        "system_language": "زبان سیستم",
        "commercial_disabled_caption": "ماژول‌های تجاری در نسخه دمو آکادمیک غیرفعال هستند.",

        # Navigation
        "nav_research_engine": "موتور پژوهش",
        "nav_system_telemetry": "پایش سیستم",
        "nav_methods": "روش‌شناسی و محدودیت‌ها",
        "nav_deep_audit": "ممیزی عمیق",
        "nav_data_lineage_vault": "مخزن ردپای داده",

        # Status
        "status_infrastructure": "زیرساخت",
        "status_online": "فعال",
        "status_mode": "حالت",
        "status_academic_dss": "سامانه پشتیبان تصمیم پژوهشی",
        "status_model": "مدل",

        # Research page
        "research_title": "موتور پژوهشی VeriClaim",
        "research_subtitle": "کشف شواهد و اولویت‌بندی ادعاهای علمی برای جریان‌های پژوهشی متن‌باز.",
        "scientific_claim": "ادعای علمی",
        "claim_placeholder": "مثلاً: Microplastics are detectable in human blood",
        "initiate_verification": "شروع اعتبارسنجی",
        "active_workspace": "محیط فعال بررسی",
        "refine_query": "اصلاح پرس‌وجو",
        "reevaluate": "ارزیابی دوباره",
        "reset_workspace": "بازنشانی محیط",

        # Pipeline messages
        "no_local_evidence": "برای '{query}' شواهد محلی پیدا نشد. اجرای n8n و OpenAlex شروع می‌شود...",
        "pipeline_progress": "بازیابی OpenAlex و اولویت‌بندی ادعا با LLM در حال انجام است...",
        "pipeline_completed": "Pipeline کامل شد. مخزن داده پژوهشی در حال به‌روزرسانی است...",
        "pipeline_failed": "Pipeline ناموفق بود. اجرای n8n و اطلاعات اتصال Postgres را بررسی کنید.",
        "no_vectors_persisted": "هنوز هیچ بردار شواهدی برای این پرس‌وجو ذخیره نشده است.",
        "gateway_fault": "خطای Gateway: اتصال به orchestrator n8n برقرار نشد.",
        "pipeline_timeout": "زمان اجرای Pipeline بیش از حد مجاز شد.",

        # Analytics
        "epistemic_overview": "نمای کلی اجماع معرفتی",
        "mean_reliability": "میانگین شاخص اتکاپذیری",
        "evidence_vectors": "بردارهای شواهد",
        "mean_certainty": "میانگین قطعیت",
        "aggregated_citations": "مجموع ارجاعات",
        "found_vectors": "{count} بردار شواهد امتیازدهی‌شده یافت شد.",

        # Cards
        "supported": "پشتیبانی‌شده",
        "mixed": "ترکیبی / قابل بحث",
        "refuted": "ردشده",
        "insufficient_evidence": "شواهد ناکافی",
        "citations": "ارجاعات",
        "year": "سال",
        "extracted_claim": "ادعای استخراج‌شده",
        "model_rationale": "استدلال مدل",
        "reliability_index": "شاخص اتکاپذیری",
        "source": "منبع",

        # Dashboard
        "dashboard_title": "پایش سیستم و بینش‌های معرفتی",
        "dashboard_subtitle": "نمای عملیاتی از مخزن داده پژوهشی VeriClaim",
        "total_articles": "کل مقاله‌ها",
        "total_claims": "کل ادعاها",
        "total_verifications": "کل ارزیابی‌ها",
        "open_access": "دسترسی آزاد",
        "total_citations": "مجموع ارجاعات",
        "verdict_distribution": "توزیع ارزیابی‌ها",
        "domain_distribution": "توزیع حوزه‌های علمی",
        "recent_vectors": "بردارهای شواهد اخیر",
        "no_dashboard_data": "هنوز داده‌ای برای پایش وجود ندارد. ابتدا یک ادعای علمی را اجرا کنید.",

        # Vault
        "vault_title": "مخزن ردپای داده",
        "vault_subtitle": "لایه ذخیره‌سازی قابل ممیزی برای ادعاها، ارزیابی‌ها و منابع شواهد",
        "filter_vault": "فیلتر مخزن",
        "filter_placeholder": "فیلتر بر اساس عنوان، ادعا، ارزیابی یا حوزه...",
        "export_csv": "خروجی CSV از مخزن فیلترشده",
        "no_vault_data": "هنوز رکوردی در مخزن ردپای داده وجود ندارد.",
        "title": "عنوان",
        "claim": "ادعا",
        "verdict": "ارزیابی",
        "domain": "حوزه",
        "verified_at": "زمان ارزیابی",
        "publication_year": "سال انتشار",

        # Deep Audit
        "deep_audit_title": "ممیزی عمیق",
        "deep_audit_subtitle": "طرح مفهومی برای اعتبارسنجی دسته‌ای فایل‌های PDF و CSV",
        "deep_audit_stub": "این ماژول در نسخه دمو آکادمیک عمداً به عنوان مسیر توسعه پژوهشی نگه داشته شده است.",
        "planned_workflow": "جریان کاری پیشنهادی:",
        "deep_audit_step_1": "پژوهشگر یک فایل PDF یا CSV بارگذاری می‌کند.",
        "deep_audit_step_2": "Streamlit فایل را به یک webhook اختصاصی در n8n ارسال می‌کند.",
        "deep_audit_step_3": "n8n ادعاهای علمی احتمالی را استخراج کرده و در PostgreSQL ذخیره می‌کند.",
        "deep_audit_step_4": "Pipeline اعتبارسنجی، ادعاهای استخراج‌شده را به‌صورت غیرهمزمان پردازش می‌کند.",
        "deep_audit_step_5": "مخزن ردپای داده خروجی‌های قابل ممیزی، منابع شواهد و متادیتای پردازش را نمایش می‌دهد.",
        "deep_audit_mvp_note": "موتور فعلی تک‌ادعا مسیر پایدار MVP است. پردازش دسته‌ای عمداً به بعد از پایدار شدن workflow OpenAlex، schema دیتابیس و کارت‌های شواهد موکول شده است.",
        "upload_future": "آپلود PDF یا CSV برای workflow آینده ممیزی دسته‌ای",
        "batch_disabled": "آپلود دسته‌ای در این نسخه دمو فاند غیرفعال است و به عنوان گام بعدی مستند شده است.",

        # Methods page extended
        "methods_positioning_body": "VeriClaim یک سامانه پشتیبان تصمیم پژوهشی برای اولویت‌بندی ادعاهای علمی است. این سامانه ادعا نمی‌کند که جایگزین داوری همتا، مرور نظام‌مند، متخصصان حوزه یا قضاوت بالینی/علمی می‌شود.",
        "methods_pipeline_intro": "نمونه اولیه آکادمیک فعلی از یک pipeline چهارمرحله‌ای پیروی می‌کند:",
        "methods_claim_intake_title": "دریافت ادعا",
        "methods_claim_intake_body": "کاربر یک ادعای علمی یا پرسش پژوهشی وارد می‌کند.",
        "methods_query_compression_title": "فشرده‌سازی پرس‌وجو",
        "methods_query_compression_body": "یک LLM ورودی را به یک عبارت جست‌وجوی کوتاه و مناسب برای OpenAlex تبدیل می‌کند.",
        "methods_evidence_retrieval_title": "بازیابی شواهد",
        "methods_evidence_retrieval_body": "متادیتای OpenAlex، چکیده‌ها، تعداد ارجاعات، لینک‌های DOI و متادیتای موضوعی بازیابی می‌شوند.",
        "methods_evidence_scoring_title": "امتیازدهی شواهد",
        "methods_evidence_scoring_body": "یک LLM ادعای اصلی را استخراج کرده و یک ارزیابی اولیه و امتیاز اطمینان اختصاص می‌دهد.",
        "methods_reliability_body": "امتیاز اتکاپذیری یک سیگنال پژوهشی اکتشافی است، نه گواهی حقیقت. در نسخه دمو فعلی، این امتیاز از سرعت ارجاع‌گیری، قطعیت زبانی، شفافیت دسترسی آزاد و تازگی انتشار ترکیب می‌شود.",
        "methods_supported_definition": "بردار شواهد ظاهراً از ادعای استخراج‌شده پشتیبانی می‌کند.",
        "methods_mixed_definition": "بردار شواهد مقدماتی، مبهم یا تا حدی متناقض است.",
        "methods_refuted_definition": "بردار شواهد ظاهراً با ادعای استخراج‌شده در تضاد است.",
        "methods_insufficient_definition": "چکیده یا متادیتا برای ارزیابی معنادار کافی نیست.",
        "methods_limitation_abstract": "تحلیل در سطح چکیده ممکن است جزئیات روش‌شناختی مهم مقاله کامل را از دست بدهد.",
        "methods_limitation_citations": "تعداد ارجاعات معادل اعتبار علمی نیست.",
        "methods_limitation_llm": "ارزیابی‌های تولیدشده توسط LLM ممکن است به نوع prompt و کیفیت متادیتا حساس باشند.",
        "methods_limitation_sources": "نمونه اولیه فعلی فقط از OpenAlex استفاده می‌کند؛ Semantic Scholar، PubMed، arXiv و Europe PMC توسعه‌های آینده هستند.",
        "methods_limitation_consensus": "ادبیات متناقض هنوز به شکل یک گراف اجماع بین‌مقاله‌ای کامل مدل‌سازی نشده است.",
        "methods_intended_use_body": "این سامانه برای کشف پژوهشی در مراحل اولیه، نقشه‌برداری شواهد، نمایش مدیریت داده پژوهشی و نمونه‌سازی بازتولیدپذیر open-science طراحی شده است.",
        "methods_demo_framing": "چارچوب پیشنهادی دمو: کشف شواهد و اولویت‌بندی ادعا، نه حقیقت علمی خودکار.",

        # Academic positioning
        "not_peer_review": "این سامانه جایگزین داوری همتا یا تخصص انسانی نیست.",
        "evidence_level_note": "ارزیابی‌ها سیگنال‌های مرتبط با شواهد هستند، نه تصمیم نهایی درباره حقیقت ادعا.",
        "future_consensus_layer": "لایه اجماع بین‌مقاله‌ای به عنوان گام پژوهشی بعدی در نظر گرفته شده است.",
    },
}


def get_lang_code(language_label: str) -> str:
    return LANGUAGE_OPTIONS.get(language_label, "en")


def t(key: str, language_label: str = "English", **kwargs) -> str:
    lang = get_lang_code(language_label)
    value = TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(
        key,
        TRANSLATIONS["en"].get(key, key),
    )

    if kwargs:
        try:
            return value.format(**kwargs)
        except Exception:
            return value

    return value


def current_language() -> str:
    try:
        import streamlit as st
        return st.session_state.get("language", "English")
    except Exception:
        return "English"


def tr(key: str, **kwargs) -> str:
    return t(key, current_language(), **kwargs)


def is_rtl() -> bool:
    return get_lang_code(current_language()) == "fa"