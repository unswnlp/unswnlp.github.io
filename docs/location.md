# Location

The Location page is a single file: `content/location.md`. There's nothing to
add over time — just edit this file in place if the group's building or
address changes.

```yaml
---
title: "Location"
date: 2024-05-08
hidemeta: true
layout: "location"

building: "School of Computer Science and Engineering"
buildingCode: "K17"
university: "The University of New South Wales"
suburb: "Sydney NSW 2052"
country: "Australia"

mapEmbed: "https://www.google.com/maps/embed?pb=..."   # Google Maps "Embed a map" iframe src
mapLink: "https://maps.google.com/?q=..."               # plain link shown alongside the embed
---
```

To get `mapEmbed`, open the location in Google Maps, use Share > Embed a map,
and copy the `src` attribute of the generated `<iframe>`.
