from pathlib import Path

import geopandas as gpd

geojson_file = Path('./pdx_crime_events.geojson')

# Read the GeoJSON file
gdf = gpd.read_file(geojson_file)

# Transform to CRS84 (EPSG:4326) if not already
if gdf.crs != 'EPSG:4326':
    gdf = gdf.to_crs('EPSG:4326')

# Write to GeoJSON file back
gdf.to_file(geojson_file, driver='GeoJSON')

# Display the transformed GeoDataFrame
print(gdf.head())
print(f"\nCurrent CRS: {gdf.crs}")


