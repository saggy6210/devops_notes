1. Azure Storage Account: 

Types of storage accounts: 
1. General-purpose v2 accounts: Basic storage account type for blobs, files, queues, and tables. | Hot, Cool, Archive | LRS, GRS, RA-GRS, ZRS, GZRS
2. General-purpose v1 accounts: Legacy account type for blobs, files, queues, and tables. | LRS, GRS, RA-GRS 
3. BlockBlobStorage accounts: Storage accounts with premium performance characteristics for block blobs and append blobs | LRS, ZRS
4. FileStorage accounts: Files-only storage accounts with premium performance characteristics. | LRS, ZRS
5. BlobStorage accounts: Legacy Blob-only storage accounts. | Hot, Cool, Archive | LRS, GRS, RA-GRS

Access tiers: 
1. Hot :  higher storage costs | expected to be accessed frequently.
2. Cool :  lower storage costs than hot tier | expected to be accessed less frequently.
3. The archive access tier has the lowest storage cost. But it has higher data retrieval costs compared to the hot and cool tiers. Data must remain in the archive tier for at least 180 days or be subject to an early deletion charge.
 
 Storage Redundancy: 
 Azure Storage account is always replicated three times in the primary region.
 1. Locally redundant storage (LRS) copies your data synchronously three times within a single physical location in the primary region. LRS is the least expensive.
 2. Zone-redundant storage (ZRS) replicates your Azure Storage data synchronously across three Azure availability zones in the primary region. 
 3. Geo-redundant storage (GRS) copies your data synchronously three times within a single physical location in the primary region using LRS. It then copies your data asynchronously to a single physical location in the secondary region.
 4. Geo-zone-redundant storage (GZRS) copies your data synchronously across three Azure availability zones in the primary region using ZRS. It then copies your data asynchronously to a single physical location in the secondary region.
